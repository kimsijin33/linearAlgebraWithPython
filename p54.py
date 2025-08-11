
def zero_mat(n, p):
    """
    영 행렬 생성
    """
    Z = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(0)
        Z.append(row)
    return Z
