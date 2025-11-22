def central_difference(func, x0: float, h: float = 1e-6, order: int = 1):
    """
        Calculates the numerical derivative of function f(x) at point x0
        using the central difference formula (recursively for any order n).

        This method is of second-order accuracy (O(h^2)).

        Args:
            func: The function to be differentiated (callable).
            x0: The point at which to calculate the derivative.
            h: The step size (must be small and positive). Defaults to 1e-6.
            order: The order of the derivative (integer >= 1). Defaults to 1.

        Returns:
            float: The numerical value of the n-th order derivative.

        Raises:
            ValueError: If h is non-positive (h <= 0) or order is less than 1.
        """
    if h <= 0:
        raise ValueError("h must be > 0")
    if order < 1:
        raise ValueError("order must be >= 1")


    if order == 1:
        return (func(x0 + h) - func(x0 - h)) / (2 * h)

    else:
        def derivative_of_prev_order(x):
            return central_difference(func, x, h, order=order - 1)

        return central_difference(derivative_of_prev_order, x0, h, order=1)