# coding: utf-8


import copy
from math import sqrt, sin, cos, isclose


def find_determinant(M) -> float:
    """Wrapper function for 'determinant'"""
    if all(len(row) == len(M) for row in M):
        return determinant(M)
    else:
        raise ValueError('Non-square matrix')


def determinant(M, det=0) -> float:
    """Обчислення детермінанта квадратної матриці M розмірності N >= 2 """
    ind = list(range(len(M)))
    if len(M) == 2 and len(M[0]) == 2:
        return M[0][0] * M[1][1] - M[1][0] * M[0][1]        
    for i in ind:
        A = copy.deepcopy(M)[1:]
        for j in range(len(A)):
            A[j] = A[j][0:i] + A[j][i+1:]
        sign = (-1) ** (i % 2)
        temp_det = determinant(A)
        det += sign * M[0][i] * temp_det
    return det


def norm(a: list) -> float:
    """Евклідова норма вектора довільної розмірності
    
    a - список координат вектора 
    """
    return sqrt(sum(i**2 for i in a))


def scale(a: list, C: float) -> list:
    """Множення вектора довільної розмірності на скаляр
    
    a - список координат вектора
    C - скаляр 
    """
    return [i*C for i in a]


def add_vectors(a: list, b: list) -> list:
    """Сума двох векторів довільної розмірності
    
    a, b - списки координат векторів
    """
    return [i + j for i, j in zip(a, b)]


def subtract_vectors(a: list, b: list) -> list:
    """Різниця двох векторів довільної розмірності
    
    a, b - списки координат векторів
    """
    if len(a) == len(b):
        return [i - j for i, j in zip(a, b)]
    else: 
        raise ValueError


def dot_product(a: list, b: list) -> float:
    """Скалярний добуток двох векторів довільної розмірності
    
    a, b - списки координат векторів
    """
    if len(a) == len(b):
        return sum(i * j for i, j in zip(a, b))
    else: 
        raise ValueError


def cross_product(a: list, b: list) -> list:
    """Векторний добуток двох векторів у просторі
    
    a, b - списки координат векторів
    """
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c
   
    
def mixed_product(a: list, b: list, c: list) -> float:
    """Мішаний добуток трьох векторів у просторі
    
    a, b, c - списки координат векторів
    """
    return find_determinant([a, b, c])


def points_dist(M: list, N: list) -> float:
    """Евклідова відстань
    
    M, N - координати точок
    """
    return sqrt(sum([(i - j) ** 2 for i, j in zip(M, N)]))


def move_point(M: list, vector: list) -> list:
    """Переміщення точки вздовж вектора
    
    vector - координати вектора
    M - координати точки
    """
    return add_vectors(M, vector)


def turn_x_point(M: list, phi: float) -> list:
    """Поворот точки M відносно осі OX на кут phi"""
    return [M[0], M[1] * cos(phi) - M[2] * sin(phi), M[1] * sin(phi) + M[2] * cos(phi)]


def turn_y_point(M: list, phi: float) -> list:
    """Поворот точки M відносно осі OY на кут phi"""
    return [M[0] * cos(phi) - M[2] * sin(phi), M[1], M[0] * sin(phi) + M[2] * cos(phi)]


def turn_z_point(M: list, phi: float) -> list:
    """Поворот точки M відносно осі OZ на кут phi"""
    return [M[0] * cos(phi) - M[1] * sin(phi), M[0] * sin(phi) + M[1] * cos(phi), M[2]]


def check_plane_correctness(coef: list) -> bool:
    """Перевірка корректності задання площини Ax+By+Cz+D=0
    
    coef - список коефіцієнтів A,B,C,D загального рівняння площини
    """
    return not isclose(sum(abs(i) for i in coef[:-1]), 0)


def get_plane(M: list, N: list, P: list) -> list:
    """Отримання списку коефіцієнтів A,B,C,D загального рівняння площини
    за допомогою трьох точок M, N, P, через які вона проходить
    """
    v1 = subtract_vectors(P, M)
    v2 = subtract_vectors(N, M)
    A, B, C = cross_product(v1, v2)
    D = -sum(i*j for i, j in zip((A, B, C), M))
    return [A, B, C, D]


def point_on_plane(coef: list, p: list) -> bool:
    """Перевірка принадлежності точки площині
    
    coef - список коефіцієнтів A,B,C,D загального рівняння площини
    p - координати точки у просторі
    """
    return isclose(coef[0] * p[0] + coef[1] * p[1] + coef[2] * p[2]+ coef[3], 0)


def point_on_line(coef1: list, coef2: list, p: list) -> bool:
    """Перевірка принадлежності точки лінії. 
    Лінія визначається перетином двох площин
    
    coef1 - список коефіцієнтів A,B,C,D загального рівняння першої площини
    coef2 -список коефіцієнтів A,B,C,D загального рівняння другої площини
    p - координати точки
    """
    return point_on_plane(coef1, p) and point_on_plane(coef2, p)


def norm_plane(coef: list) -> list:
    """Нормування площини
    
    coef - список коефіцієнтів A,B,C,D загального рівняння площини
    """
    n = sqrt(sum(i**2 for i in coef[:-1]))
    return [i / n for i in coef]


def point_to_plane_dist(coef: list, p: list) -> float:
    """Відстань від точки до площини
    
    coef - список коефіцієнтів A,B,C,D загального рівняння площини
    p - координати точки у просторі
    """
    if check_plane_correctness(coef):
        ncoef = norm_plane(coef)
        return ncoef[0] * p[0] + ncoef[1] * p[1] + ncoef[2] * p[2] + ncoef[3]
    else:
        raise ValueError

        
def three_planes_intersect(coef1: list, coef2: list, coef3: list) -> list:
    """Знаходження точки перетину трьох площин
    
    coef1, coef2, coef3 - списки коефіцієнтів A,B,C,D загальних рівнянь площин
    """
    c1 = check_plane_correctness(coef1[:-1])
    c2 = check_plane_correctness(coef2[:-1])
    c3 = check_plane_correctness(coef3[:-1])
    if c1 and c2 and c3:
        det = find_determinant([coef1[:-1], coef2[:-1], coef3[:-1]])
        print(det)
        if not isclose(det, 0):
            d = [coef1[-1], coef2[-1], coef3[-1]]
            detX = determinant([[coef1[-1], coef1[1], coef1[2]],
                                [coef2[-1], coef2[1], coef2[2]],
                                [coef3[-1], coef3[1], coef3[2]]])
            detY = determinant([[coef1[0], coef1[-1], coef1[2]],
                                [coef2[0], coef2[-1], coef2[2]],
                                [coef3[0], coef3[-1], coef3[2]]])
            detZ = determinant([[coef1[0], coef1[1], coef1[-1]],
                                [coef2[0], coef2[1], coef2[-1]],
                                [coef3[0], coef3[1], coef3[-1]]])

            return [-detX / det, -detY / det, -detZ / det]
        else:
            return None
    else:
        raise ValueError
      
    
def proj_point_on_plane(coef: list, p: list) -> list:
    """Проекція точки на площину
    
    coef - список коефіцієнтів A,B,C,D загального рівняння площини
    p - координати точки у просторі
    """
    if check_plane_correctness(coef):
        A, B, C, D = coef
        t = - (A*p[0] + B*p[1] + C*p[2] + D) / (A**2 + B**2 + C**2)
        return [A*t + p[0], B*t + p[1], C*t + p[2]]
    else:
        raise ValueError
    

def triangle_area_2d(A: list, B: list, C: list) -> float:
    """Обчислення площі трикутника на площині
    
    A, B, C - координати вершин
    """
    v1 = subtract_vectors(B, A)
    v2 = subtract_vectors(C, A)
    return 0.5 * abs(find_determinant([v1, v2]))


def triangle_area_3d(A: list, B: list, C: list) -> float:
    """Обчислення площі трикутника у просторі
    
    A, B, C - координати вершин
    """
    v1 = subtract_vectors(B, A)
    v2 = subtract_vectors(C, A)
    return 0.5 * norm(cross_product(v1, v2))
