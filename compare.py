import numpy as np


s = input()
f1 = s[:s.find('txt') + 3]
f2 = s[s.find('txt') + 4:]

print("Start working...")

pairs = open(f1, 'r')
scores = open(f2, 'w')


def check_letters(letter_1, letter_2):
    return 0 if letter_1 == letter_2 else 1


def space_delete(S):
    s = ''
    tmp = 1
    for i in S:
        if tmp:
            s += i
        if i == ' ':
            tmp = 1 - tmp
    return s


def matrix_D(S1: str, S2: str, M: int, N: int):
    D = np.zeros((M+1, N+1))
    for i in range(1, M+1):
        D[i, 0] = i
    for j in range(1, N+1):
        D[0, j] = j
    for i in range(1, M+1):
        for j in range(1, N+1):
            D[i, j] = min(D[i, j-1] + 1, D[i-1,j] + 1, D[i-1,j-1] + check_letters(S1[i-1], S2[j-1]))
    return D

for i in pairs.readlines():
    path_1 = i.strip().split()[0].replace('\\', '/')
    path_2 = i.strip().split()[1].replace('\\', '/')
    file_1 = open(path_1, 'r')
    file_2 = open(path_2, 'r')
    S1 = file_1.read()
    S1 = space_delete(S1.lower())
    S2 = file_2.read()
    S2 = space_delete(S2.lower())
    if len(S1) == 0 or len(S2) == 0:
        scores.write(str(1) + '\n')
    else:
        scores.write(str(matrix_D(S1, S2, len(S1),len(S2))[len(S1)][len(S2)]/max(len(S1),len(S2))) + '\n')

    file_1.close()
    file_2.close()


pairs.close()
scores.close()
print("Work was done")