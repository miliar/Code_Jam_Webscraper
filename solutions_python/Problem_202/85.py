import numpy as np

def solve_problem(grid_size, models_data):
    g = grid_size
    p_mat = np.zeros([g, g], dtype = bool)
    p_mat_add = np.zeros([g, g], dtype = bool)
    x_mat = np.zeros([g, g], dtype = bool)
    x_mat_add = np.zeros([g, g], dtype = bool)
    for model in models_data:
        model = model.split(" ")
        if model[0] != "x":
            p_mat[int(model[1]) - 1][int(model[2]) - 1] = True
        
        if model[0] != "+":
            x_mat[int(model[1]) - 1][int(model[2]) - 1] = True
    
    v_mat = []
    h_mat = []
    for k in range(g):
        h_mat.append(np.zeros([g, g], dtype = bool))
        h_mat[k][k] += np.ones([g], dtype = bool)
        v_mat.append(np.zeros([g, g], dtype = bool))
        v_mat[k] = h_mat[k].T
    
    ban_mat = np.zeros([g, g], dtype = bool)
    for i in range(g):
        for j in range(g):
            if x_mat[i][j]:
                ban_mat += h_mat[i]
                ban_mat += v_mat[j]
                
    for i in range(g):
        for j in range(g):
            if not ban_mat[i][j]:
                x_mat[i][j] = True
                x_mat_add[i][j] = True
                ban_mat += h_mat[i]
                ban_mat += v_mat[j]
                    
    d_dia = {}
    u_dia = {}
    for k in range(-g+1, g):
        d_dia[k] = np.zeros([g, g], dtype = bool)
    for k in range(2*g - 1):
        u_dia[k] = np.zeros([g, g], dtype = bool)
    
    for i in range(g):
        for j in range(g):
            d_dia[i - j][i][j] = True
            u_dia[i + j][i][j] = True
    
    ban_mat = np.zeros([g, g], dtype = bool)
    for i in range(g):
        for j in range(g):
            if p_mat[i][j]:
                ban_mat += d_dia[i - j]
                ban_mat += u_dia[i + j]
    
    w = 0
    while w <= g - 1 - w:
        for i in range(w, g - w):
            for j in [w, g - 1 - w]:
                if not ban_mat[i][j]:
                    p_mat[i][j] = True
                    p_mat_add[i][j] = True
                    ban_mat += d_dia[i - j]
                    ban_mat += u_dia[i + j]
                    
        for j in range(w, g - w):
            for i in [w, g - 1 - w]:
                if not ban_mat[i][j]:
                    p_mat[i][j] = True
                    p_mat_add[i][j] = True
                    ban_mat += d_dia[i - j]
                    ban_mat += u_dia[i + j]
        
        w += 1
    
    """
    for i in range(g):
        for j in range(g):
            if not ban_mat[i][j]:
                p_mat[i][j] = True
                p_mat_add[i][j] = True
                ban_mat += d_dia[i - j]
                ban_mat += u_dia[i + j]
    """
    
    add_models = []
    for i in range(g):
        for j in range(g):
            if (p_mat_add[i][j] or x_mat_add[i][j]):
                if (p_mat[i][j] and x_mat[i][j]):
                    add_models.append("o %d %d" %(i+1, j+1))
                elif p_mat[i][j]:
                    add_models.append("+ %d %d" %(i+1, j+1))
                elif x_mat[i][j]:
                    add_models.append("x %d %d" %(i+1, j+1))
    
    return (p_mat.sum() + x_mat.sum(), (p_mat_add + x_mat_add).sum(), add_models)


def phase():
    grid, model_n = input().split(" ")
    grid = int(grid)
    model_n = int(model_n)
    model_list = []
    for m in range(model_n):
        model_list.append(input())
    
    out_put = {"grid" : grid,
               "models" : model_list
              }
    return out_put
    

def main():
    test_times = int(input())
    for t in range(1, test_times + 1):
        phase_info = phase()
        result = solve_problem(phase_info["grid"], phase_info["models"])
        
        print ("Case #%d: %d %d" %(t, result[0], result[1]))
        
        for add_m in result[2]:
            print (add_m)

if __name__ == "__main__":
    main()