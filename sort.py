N, k = map(int, input().split())
L = list(map(int, input().split()))


def quick_select(L, k):
    p = L[0]
    A, B, M = [], [], []
    for x in L:
        if p > x:
            A.append(x)
        elif p < x:
            B.append(x)
        else:
            M.append(x)
    if len(A) > k:
        return quick_select(A, k)
    elif len(A)+len(M) <= k:
        k = k-len(A)-len(M)
        return quick_select(B, k)
    else:
        return p


print(quick_select(L, k-1))
