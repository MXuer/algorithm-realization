import numpy as np

def eucl(a, b):
    return abs(a - b)

def dist_mat(x, y):
    M = np.zeros(shape=(len(x), len(y)), dtype=int)
    for i in range(len(x)):
        for j in range(len(y)):
            M[i, j] = eucl(x[i], y[j])
    
    return M

def cost_m(M):
    num_v = np.shape(M)[0]
    num_h = np.shape(M)[1]
    Mc = np.zeros(np.shape(M), M.dtype)
    Mc[0][0] = M[0][0]
    for i in range(1, num_v):
        Mc[i, 0] = Mc[i - 1, 0] + M[i, 0]
    for j in range(1, num_h):
        Mc[0, j] = Mc[0, j - 1] + M[0, j]
    
    for i in range(1, num_v):
        for j in range(1, num_h):
            Mc[i, j] = min(Mc[i-1, j-1], Mc[i-1, j], Mc[i, j-1]) + M[i, j]
        
    return Mc
    
x = [3, 5, 6, 7, 7, 1]
y = [3, 6, 6, 7, 8, 1, 1]
z = [2, 5, 7, 7, 7, 7, 2]
print (x, y, z)
M_xy = dist_mat(x, y)
M_xz = dist_mat(x, z)
Mc_xy = cost_m(M_xy)
Mc_xz = cost_m(M_xz)
print(M_xy)
print(Mc_xy)
print(M_xz)
print(Mc_xz)