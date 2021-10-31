def find_missing_nums(nums):

    n = nums[-1] + 1
    sravn = list(range(1, n+1))
    b = []
    for c in sravn:
        if c in nums:
            pass
        else:
            b.append(c)
    return b
