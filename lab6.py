"""1.	Формируется матрица F следующим образом: скопировать в нее А и если количество нулей в В больше, чем в Е,
то поменять в ней местами В и С симметрично, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется.
 После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * F,
иначе вычисляется выражение (A-1 +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно. """

import numpy as np
import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

N = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 4 до 100: "))
while N < 4 or 100 < N:
    N = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 4 до 100: "))

K = int(input("Введите число К: "))
start = time.time()

A = np.random.randint(-10, 10, (N, N)) #заполняем матрицу А случайными числами
print("Матрица А")
print(A)

F = A.copy()           #копируем элементы матрицы А в матрицу F
print("Матрица F")
print(F)

if np.count_nonzero(F[0: N//2: 1, 0: N//2: 1]) < np.count_nonzero(F[N//2: N:1, N//2: N: 1]):
    for i in range(N//2):
        for j in range(N//2):
            F[i][j + N//2 + N % 2], F[N - 1 - i][j + N//2 + N % 2] = F[N - 1 - i][j + N//2 + N % 2], F[i][j + N//2 + N % 2]
else:
    for i in range(N//2):
        for j in range(N//2):
            F[i][j], F[i][N // 2 + N % 2 + j] = F[i][N // 2 + N % 2 + j], F[i][j]
print("Матрица F")
print(F)

G = np.tril(A, k=0)             #формируем матрицу из нижнего тругольника матрицы А
print("Матрица G")
print(G)

if np.linalg.det(A) > np.trace(F):
    print("A*AT – K * F")
    print(np.dot(np.array(A),(np.transpose(A)))-K*F)
else:
    print("(A-1 +G-F-1)*K")
    print((np.linalg.inv(A)+G-(np.linalg.inv(F)))*K)

fig, ax = plt.subplots()                                #matplotlib
ax.set(xlabel='column number', ylabel='value')
for i in range(N):
    for j in range(N):
        plt.bar(i, F[i][j])
plt.show()

fig, ax = plt.subplots()
ax.set(xlabel='column number', ylabel='value')
ax.grid()
for j in range(N):
    ax.plot([i for i in range(N)], F[j][::])
plt.show()

ax = plt.figure().add_subplot(projection='3d')
ax.set(xlabel='x', ylabel='y', zlabel='z')
for i in range(N):
    plt.plot([j for j in range(N)], F[i][::], i)
plt.show()


sns.heatmap(data = F, annot = True)                 #seaborn
plt.xlabel('column number')
plt.ylabel('row number')
plt.show()

sns.boxplot(data = F)
plt.xlabel('column number')
plt.ylabel('value')
plt.show()

sns.lineplot(data = F)
plt.xlabel('column number')
plt.ylabel('value')
plt.show()
sns.set_theme(style="darkgrid")

sns.set_theme(style="white")
df = sns.load_dataset("penguins")

