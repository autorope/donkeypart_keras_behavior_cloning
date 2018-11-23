# -*- coding: utf-8 -*-
import pytest
from donkeypart_keras_behavior_cloning import KerasPilot, KerasLinear
from donkeypart_keras_behavior_cloning.part import default_linear


def test_linear():
    kl = KerasLinear()
    assert kl.model is not None


def test_linear_with_model():
    kc = KerasLinear(default_linear())
    assert kc.model is not None

