#!/usr/bin/env python3
from typing import List

def pascal_triangle(n: int) -> List[List[int]]:
    '''
    Generate Pascal's triangle up to the given number of rows

    Args:
        n (int): Number of rows to generate in Pascal's triangle

    Returns:
        List[List[int]]: Pascal's triangle represented as a list of lists of integers
    '''
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(0, len(triangle[-1]) - 1):
            a = triangle[-1][j]
            b = triangle[-1][j+1]
            temp.insert(-1, a + b)
        triangle.append(temp)

    return triangle
