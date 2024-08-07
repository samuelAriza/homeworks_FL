N = 6
E = ["a"]
F = [1, 4]
M = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5,0]]

minimitation = []

c = 1
c_ = 0

flag = False

equivalent = []

def search(n, n_1):
    T = []
    for row in M:
        if row[0] == n:
            T.append(row.copy())
        elif row[0] == n_1:
            T.append(row.copy())
    return T

for i in range(0, N):
    minimitation.append([])
    for j in range(0, N):
        if i == j:
            minimitation[i].append(i)
        else:
            minimitation[i].append('_')

for i in range(0, N - 1):
    for j in range(i + 1, N):
        print(f"[{i}, {i}] [{j}, {j}]")
        if minimitation[i][i] in F and minimitation[j][j] not in F or minimitation[i][i] not in F and minimitation[j][j] in F:
            minimitation[j][i] = 'x'

#c = 1
#c_ = 0
#step_3(c, N - c)
def step_3(v, v_1):   
    
    flag = False

    global c 
    global c_ 
    global N
    global M

    if N - c != 0:
        print("-------")
        print(v)
        print(v_1)
        print("-------")
        for i in range(v, v_1):
            print(f"({i}, {c_})")
            if minimitation[i][c_] == '_':
                print(f"{c_}, {i}")
                T = search(c_, i)
                print("Hola")
                print(T)
                print(T[0])
                print(T[1])
                T[0].pop(0)
                T[1].pop(0)
                print(T)
                print("####")
                print(M)
                print("####")
                while flag == False and len(T[0]) > 0:
                    print(T)
                    f = T[0].pop(0)
                    f_1 = T[1].pop(0)
                    print(f)
                    print(f_1)
                    row = max(f, f_1)
                    col = min(f, f_1)
                    print("-------")
                    print(row)
                    print(col)
                    print("-------")
                    if minimitation[row][col] == 'x':
                        print("XXXXXXXXXXXXXXXXXXXXXXXXXX")
                        minimitation[i][c_] = 'x'
                        flag = True
        c = c + 1
        c_ = c_ + 1

        step_3(c, N)

        if flag:
            c = 1
            c_ = 0
            step_3(c, N)
            






def search_equivalent(w, w_1):
    global c 
    global c_ 
    global N
    global M
    global equivalent

    if N - c != 0:
        for i in range(w, w_1):
            print(f"({i}, {c_})")
            if minimitation[i][c_] == '_':
                pair = (min(i, c_), max(i, c_))
                equivalent.append(pair)
        c = c + 1
        c_ = c_ + 1
        search_equivalent(c, N)
    return equivalent

step_3(c, N - c)

for row in minimitation:
    print(row)

c = 1
c_ = 0

print(search_equivalent(c, N - c))

