import numpy as np
def count_vowels_consonants():
    str = "Write a program to count the number of vowels and consonants present in an input string"
    str = str.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    for i in str:
        if i in vowels:
            vowel_count += 1
        elif i.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count

def matrix_multiplication(m1,m2):
    sm1 = m1.shape
    sm2 = m2.shape
    if sm1[1] != sm2[0]:
        print("Matrix multiplication not possible")
        return None
    result = []
    for i in range(sm1[0]):
        row = []
        for j in range(sm2[1]):
            sum = 0
            for k in range(sm1[1]):
                sum += m1[i][k] * m2[k][j]
            row.append(sum)
        result.append(row)
    return result
    
def find_common_elements(arr1,arr2):
    common = []
    for i in arr1:
        if i in arr2:
            common.append(i)
    return common

def transpose_matrix(matrix):
    transpose = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose

# v,c = count_vowels_consonants()
# print("Vowels: ", v)
# print("Consonants: ", c)

m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.array([[1,2],[3,4],[5,6]])
result = matrix_multiplication(m1,m2)
print("multiplication of 2 matrix: ",result)

# arr1 = [1,2,3,4,5]
# arr2 = [4,5,6,7,8]
# common = find_common_elements(arr1,arr2)
# print("Common elements: ",common)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
transpose = transpose_matrix(matrix)
print("Transpose of matrix: ",transpose)
new change



