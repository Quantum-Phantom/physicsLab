# -*- coding: utf-8 -*-

from physicsLab import _tools
from physicsLab.circuit import CircuitBase
from physicsLab.celestial import PlanetBase
from physicsLab.electromagnetism import ElectromagnetismBase
from physicsLab.enums import ExperimentType, OpenMode
from physicsLab._core import _Experiment
from physicsLab._typing import Dict, Tuple, List, num_type


class CircuitExperiment(_Experiment):
    """Experimental support for circuit experiment"""

    Wires: set
    _is_elementXYZ: bool
    _elementXYZ_origin_position: _tools.position

    def __init__(
        self,
        open_mode: OpenMode,
        # TODO 把 Tuple[num_type, num_type, num_type] 换成 _tools.position
        _position2elements: Dict[
            Tuple[num_type, num_type, num_type], List[CircuitBase]
        ],
        _id2element: Dict[str, CircuitBase],
        Elements: List[CircuitBase],
        SAV_PATH: str,
        PlSav: dict,
        CameraSave: dict,
        VisionCenter: _tools.position,
        TargetRotation: _tools.position,
        wires: set,
        is_elementXYZ: bool,
        elementXYZ_origin_position: _tools.position,
    ) -> None:
        super().__init__(
            open_mode,
            _position2elements,
            _id2element,
            Elements,
            SAV_PATH,
            PlSav,
            CameraSave,
            VisionCenter,
            TargetRotation,
            ExperimentType.Circuit,
        )
        self.Wires = wires
        self._is_elementXYZ = is_elementXYZ
        self._elementXYZ_origin_position = elementXYZ_origin_position


class CelestialExperiment(_Experiment):
    def __init__(
        self,
        open_mode: OpenMode,
        _position2elements: Dict[Tuple[num_type, num_type, num_type], List[PlanetBase]],
        _id2element: Dict[str, PlanetBase],
        Elements: List[PlanetBase],
        SAV_PATH: str,
        PlSav: Dict,
        CameraSave: Dict,
        VisionCenter: _tools.position,
        TargetRotation: _tools.position,
    ) -> None:
        super().__init__(
            open_mode,
            _position2elements,
            _id2element,
            Elements,
            SAV_PATH,
            PlSav,
            CameraSave,
            VisionCenter,
            TargetRotation,
            ExperimentType.Celestial,
        )


class ElectromagnetismExperiment(_Experiment):
    def __init__(
        self,
        open_mode: OpenMode,
        _position2elements: Dict[
            Tuple[num_type, num_type, num_type], List[ElectromagnetismBase]
        ],
        _id2element: Dict[str, ElectromagnetismBase],
        Elements: List[ElectromagnetismBase],
        SAV_PATH: str,
        PlSav: Dict,
        CameraSave: Dict,
        VisionCenter: _tools.position,
        TargetRotation: _tools.position,
    ) -> None:
        super().__init__(
            open_mode,
            _position2elements,
            _id2element,
            Elements,
            SAV_PATH,
            PlSav,
            CameraSave,
            VisionCenter,
            TargetRotation,
            ExperimentType.Electromagnetism,
        )
