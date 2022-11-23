import math


def haversine_km(lat1, lon1, lat2, lon2) -> float:
    """ Return the distance in km. """
    if lat1 == lat2 and lon1 == lon2:
        return 0.0

    v = (math.sin(lat1 * math.pi / 180) * math.sin(lat2 * math.pi / 180)
         + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180)
         * math.cos(lon2 * math.pi / 180 - lon1 * math.pi / 180))

    # take care of floating point imprecision
    if 1.0 < v < 1.01:
        v = 1.0
    elif -1.01 < v < -1.0:
        v = -1.0

    if v < -1 or v > 1:
        raise RuntimeError(f'Error in distance for {lat1}, {lon1}, {lat2}, {lon2})')

    return 1.852001 * 3443.8985 * math.acos(v)
