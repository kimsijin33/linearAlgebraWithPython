def deppcopy(A):
    """
    """
    if type(A[0]) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n,p)
        for i in range(0, n):
            for j in rang(0, p):
                res[i][j]= A[i][j]
        return res
    else:
        n = len(A)
        res = []
        for i in rang(0,n):
            res.append(A[i])
        return res
