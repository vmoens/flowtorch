# Copyright (c) FlowTorch Development Team. All Rights Reserved
# SPDX-License-Identifier: MIT

from typing import Optional, Sequence

import torch

import flowtorch
from flowtorch.param import ParamsModule


class Empty(flowtorch.Params):
    def __call__(
        self,
        input_shape: torch.Size,
        param_shapes: Sequence[torch.Size],
        context_dims: int,
    ) -> Optional[ParamsModule]:
        return None
