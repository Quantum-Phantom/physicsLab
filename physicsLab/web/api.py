''' 该文件提供协程风格的api的封装
    所有以`async_`开头的函数/方法均为协程风格的api
'''
import sys
import types
import asyncio
import functools
import threading
import contextvars
from ._api import get_avatar, get_start_page, _User
from physicsLab.enums import Tag, Category
from physicsLab._typing import Callable, Optional, List

# 从 threading._threading_atexits 中注销掉 furure._python_exit
from concurrent.futures import thread

# python3.14之前, threading.Thread.join 在 Windows 上会阻塞异常的传播
# 也就是说, 在join结束之前, Python无法及时抛出 KeyboardInterrupt
# 而 python 并未提供公开的方法操作 threading._threading_atexit
# NOTE: 依赖于 asyncio 与 concurrent.futures.thread 的实现细节
if sys.version_info < (3, 14) and hasattr(threading, "_threading_atexits"):
    _threading_atexits = [] # TODO unregister是否会导致一些问题 ?
    for fn in threading._threading_atexits:
        if isinstance(fn, types.FunctionType) and fn is not thread._python_exit:
            _threading_atexits.append(fn)
        elif isinstance(fn, functools.partial) and fn.func is not thread._python_exit:
            _threading_atexits.append(fn)
    threading._threading_atexits = _threading_atexits

async def _async_wrapper(func: Callable, *args, **kwargs):
    if sys.version_info < (3, 9):
        # copied from asyncio.to_thread
        loop = asyncio.get_running_loop()
        ctx = contextvars.copy_context()
        func_call = functools.partial(ctx.run, func, *args, **kwargs)
        return await loop.run_in_executor(None, func_call)
    else:
        return await asyncio.to_thread(func, *args, **kwargs)

async def async_get_start_page():
    return await _async_wrapper(get_start_page)

async def async_get_avatar(target_id: str, index: int, category: str, size_category: str):
    return await _async_wrapper(get_avatar, target_id, index, category, size_category)

class User(_User):
    ''' 该class提供协程风格的api '''
    async def async_get_library(self):
        return await _async_wrapper(self.get_library)

    async def async_query_experiments(
            self,
            category: Category,
            tags: Optional[List[Tag]] = None,
            exclude_tags: Optional[List[Tag]] = None,
            languages: Optional[List[str]] = None,
            user_id: Optional[str] = None,
            take: int = 18,
            skip: int = 0,
    ):
        return await _async_wrapper(
            self.query_experiments,
            category,
            tags,
            exclude_tags,
            languages,
            user_id,
            take,
            skip,
        )

    async def async_get_experiment(
            self,
            content_id: str,
            category: Optional[Category] = None,
    ) -> dict:
        return await _async_wrapper(self.get_experiment, content_id, category)

    async def async_confirm_experiment(self, summary_id: str, category: Category, image_counter: int):
        return await _async_wrapper(self.confirm_experiment, summary_id, category, image_counter)

    async def async_post_comment(
            self,
            target_id: str,
            target_type: str,
            content: str,
            reply_id: Optional[str] = None,
    ) -> dict:
        return await _async_wrapper(self.post_comment, target_id, target_type, content, reply_id)

    async def async_remove_comment(self, CommentID: str, target_type:str):
        return await _async_wrapper(self.remove_comment, CommentID, target_type)

    async def async_get_comments(
            self,
            target_id: str,
            target_type: str,
            take: int = 16,
            skip: int = 0,
    ):
        return await _async_wrapper(self.get_comments, target_id, target_type, take, skip)

    async def async_get_summary(self, content_id: str, category: Category):
        return await _async_wrapper(self.get_summary, content_id, category)

    async def async_get_derivatives(self, content_id: str, category: Category):
        return await _async_wrapper(self.get_derivatives, content_id, category)

    async def async_get_user(
            self,
            user_id: Optional[str] = None,
            name: Optional[str] = None,
    ):
        return await _async_wrapper(self.get_user, user_id, name)

    async def async_get_profile(self):
        return await _async_wrapper(self.get_profile)

    async def async_star(self, content_id: str, category: Category, status: bool = True):
        return await _async_wrapper(self.star, content_id, category, status)

    async def async_star_content(self, content_id: str, category: Category, status: bool = True):
        return await _async_wrapper(self.star_content, content_id, category, status)

    async def async_upload_image(self, policy: str, authorization: str, image_path: str):
        return await _async_wrapper(self.upload_image, policy, authorization, image_path)

    async def async_get_message(self, message_id: str):
        return await _async_wrapper(self.get_message, message_id)

    async def async_get_messages(
            self,
            category_id: int = 0,
            skip: int = 0,
            take: int = 16,
            no_templates: bool = True,
    ):
        return await _async_wrapper(self.get_messages, category_id, skip, take, no_templates)

    async def async_get_supporters(
            self,
            content_id: str,
            category: Category,
            skip: int = 0,
            take: int = 16,
    ):
        return await _async_wrapper(self.get_supporters, content_id, category, skip, take)

    async def async_get_relations(
            self,
            user_id: str,
            display_type: str = "Follower",
            skip: int = 0,
            take: int = 20,
            query: str = "",
    ):
        return await _async_wrapper(self.get_relations, user_id, display_type, skip, take, query)

    async def async_follow(self, target_id: str, action: bool = True):
        return await _async_wrapper(self.follow, target_id, action)

    async def async_rename(self, nickname: str):
        return await _async_wrapper(self.rename, nickname)

    async def async_modify_info(self, target: str):
        return await _async_wrapper(self.modify_info, target)

    async def async_receive_bonus(self):
        return await _async_wrapper(self.receive_bonus)
