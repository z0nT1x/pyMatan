def numerical_limit(func, x0:float, side: str = "both", h:float = 1e-6):
    """
        Calculates the numerical limit of the function f(x) as x approaches x0.

        This function approximates the limit by evaluating the function at points
        (x0 - h) and/or (x0 + h).

        Args:
            func: The function for which the limit is being sought (callable).
            x0: The point that x approaches.
            side: The side of approach ('left', 'right', or 'both').
                  Defaults to 'both'.
            h: The small step size used for approximation (h > 0).
               Defaults to 1e-6.

        Returns:
            float or None: The numerical value of the limit.
                           Returns None if side is 'both' and the left and
                           right limits do not agree within a tolerance.

        Raises:
            ValueError: If h is non-positive (h <= 0) or if the 'side'
                        parameter is invalid.
    """

    if h <= 0:
        raise ValueError("h should be >= 0")

    if side == "both":
        left_limit = func(x0 - h)
        right_limit = func(x0 + h)

        if abs(left_limit - right_limit) < h * 100:
            return (left_limit + right_limit) / 2
        else:
            return None

    elif side == "left":
        return func(x0 - h)

    elif side == "right":
        return func(x0 + h)

    else:
        raise ValueError("Side should be either 'left' or 'right'")
