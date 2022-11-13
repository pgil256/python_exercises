def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    for num in nums:
        (let i=0; i<=num; i++):
            is_factor = []
            if ((num%i=0) == True)
                is_factor.append(i)
            return is_factor
            