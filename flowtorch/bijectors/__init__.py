# Copyright (c) Meta Platforms, Inc

"""
Warning: This file was generated by flowtorch/scripts/generate_imports.py
Do not modify or delete!

"""

import inspect
from typing import cast, List, Tuple

import torch
from flowtorch.bijectors.affine import Affine
from flowtorch.bijectors.affine_autoregressive import AffineAutoregressive
from flowtorch.bijectors.affine_fixed import AffineFixed
from flowtorch.bijectors.autoregressive import Autoregressive
from flowtorch.bijectors.base import Bijector
from flowtorch.bijectors.compose import Compose
from flowtorch.bijectors.conv11 import Conv1x1Bijector
from flowtorch.bijectors.conv11 import SomeOtherClass
from flowtorch.bijectors.coupling import ConvCouplingBijector
from flowtorch.bijectors.coupling import CouplingBijector
from flowtorch.bijectors.elementwise import Elementwise
from flowtorch.bijectors.elu import ELU
from flowtorch.bijectors.exp import Exp
from flowtorch.bijectors.fixed import Fixed
from flowtorch.bijectors.invert import Invert
from flowtorch.bijectors.leaky_relu import LeakyReLU
from flowtorch.bijectors.permute import Permute
from flowtorch.bijectors.power import Power
from flowtorch.bijectors.sigmoid import Sigmoid
from flowtorch.bijectors.softplus import Softplus
from flowtorch.bijectors.spline import Spline
from flowtorch.bijectors.spline_autoregressive import SplineAutoregressive
from flowtorch.bijectors.tanh import Tanh
from flowtorch.bijectors.volume_preserving import VolumePreserving

standard_bijectors = [
    ("Affine", Affine),
    ("AffineAutoregressive", AffineAutoregressive),
    ("AffineFixed", AffineFixed),
    ("Fixed", Fixed),
    ("Conv1x1Bijector", Conv1x1Bijector),
    ("SomeOtherClass", SomeOtherClass),
    ("ConvCouplingBijector", ConvCouplingBijector),
    ("CouplingBijector", CouplingBijector),
    ("ELU", ELU),
    ("Exp", Exp),
    ("LeakyReLU", LeakyReLU),
    ("VolumePreserving", VolumePreserving),
    ("Power", Power),
    ("Sigmoid", Sigmoid),
    ("Softplus", Softplus),
    ("Spline", Spline),
    ("Tanh", Tanh),
]

meta_bijectors = [
    ("Elementwise", Elementwise),
    ("Autoregressive", Autoregressive),
    ("Bijector", Bijector),
    ("Compose", Compose),
    ("Invert", Invert),
    ("Permute", Permute),
    ("SplineAutoregressive", SplineAutoregressive),
]


def isbijector(cls: type) -> bool:
    # A class must inherit from flowtorch.Bijector to be considered a valid bijector
    return issubclass(cls, Bijector)


def standard_bijector(cls: type) -> bool:
    # "Standard bijectors" are the ones we can perform standard automated tests upon
    return (
        inspect.isclass(cls)
        and isbijector(cls)
        and cls.__name__ not in [clx for clx, _ in meta_bijectors]
    )


# Determine invertible bijectors
invertible_bijectors = []
for bij_name, cls in standard_bijectors:
    # TODO: Use factored out version of the following
    # Define plan for flow
    event_dim = max(cls.domain.event_dim, 1)  # type: ignore
    event_shape = event_dim * [4]
    # base_dist = dist.Normal(torch.zeros(event_shape), torch.ones(event_shape))
    bij = cls(shape=torch.Size(event_shape))

    try:
        y = torch.randn(*bij.forward_shape(event_shape))
        bij.inverse(y)
    except NotImplementedError:
        pass
    else:
        invertible_bijectors.append((bij_name, cls))


__all__ = ["standard_bijectors", "meta_bijectors", "invertible_bijectors"] + [
    cls
    for cls, _ in cast(List[Tuple[str, Bijector]], meta_bijectors)
    + cast(List[Tuple[str, Bijector]], standard_bijectors)
]
