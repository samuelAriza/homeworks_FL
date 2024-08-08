def search(n, n_1):
    T = []
    for row in M:
        if row[0] == n:
            T.append(row.copy())
        elif row[0] == n_1:
            T.append(row.copy())
    return T

def search_equivalent(w, w_1):
    global c 
    global c_ 
    global N
    global M
    global equivalent

    if N - c != 0:
        for i in range(w, w_1):
            if minimitation[i][c_] == '_':
                x = min(i, c_)
                y =  max(i, c_)
                equivalent.append(x)
                equivalent.append(y)
        c = c + 1
        c_ = c_ + 1
        search_equivalent(c, N)
    return equivalent

def first_step(n):
    for i in range(0, n):
        minimitation.append([])
        for j in range(0, n):
            if i == j:
                minimitation[i].append(i)
            else:
                minimitation[i].append('_')

def second_step(n):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if minimitation[i][i] in F and minimitation[j][j] not in F or minimitation[i][i] not in F and minimitation[j][j] in F:
                minimitation[j][i] = 'x'

def third_step(v, v_1):   
    
    flag = False

    global c 
    global c_ 
    global N
    global M

    if N - c != 0:
        for i in range(v, v_1):
            if minimitation[i][c_] == '_':
                T = search(c_, i)
                T[0].pop(0)
                T[1].pop(0)
                while flag == False and len(T[0]) > 0:
                    f = T[0].pop(0)
                    f_1 = T[1].pop(0)
                    row = max(f, f_1)
                    col = min(f, f_1)
                    if minimitation[row][col] == 'x':
                        minimitation[i][c_] = 'x'
                        flag = True
        c = c + 1
        c_ = c_ + 1

        third_step(c, N)

        if flag:
            c = 1
            c_ = 0
            third_step(c, N)
            
def collect_cases():
    cases = []
    c = int(input())

    for i in range(0, c):
        M = []
        N = int(input())
        E = [x for x in input().split(' ')]
        F = [int(x) for x in input().split(' ')]

        for j in range(0, N):
            m = [int(x) for x in input().split(' ')]
            M.append(m)

        cases.append({
            "N" : N,
            "E" : E,
            "F" : F,
            "M" : M
        })
    return cases

cases = collect_cases()

for case in cases:
    N = case["N"]
    E = case["E"]
    F = case["F"]
    M = case["M"]
    minimitation = []
    c = 1
    c_ = 0
    flag = False
    equivalent = []

    first_step(N)
    second_step(N)
    third_step(c, N - c)

    c = 1
    c_ = 0

    result = search_equivalent(c, N - c)
    print(' '.join(str(x) for x in result))