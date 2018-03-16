cpdef int csum(vals):

    cdef int total = 0
    cdef int v
    for v in vals:
        total += v

    return total