"""My own tests for minutes_per_km."""

import pytest

from orders import minutes_per_km


def test_slow_delivery():
    # 60 minutes over 6 km = 10.0 minutes/km
    assert minutes_per_km(60, 6) == 10.0


def test_negative_distance_raises():
    # Negative distance must raise ValueError
    with pytest.raises(ValueError):
        minutes_per_km(60, -3)
