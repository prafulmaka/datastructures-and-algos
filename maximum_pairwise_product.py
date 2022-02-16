import time

# This approach takes more time and memory
# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#     return max_product

# This approach is faster and consumes less memory
def max_pairwise_product(numbers):
    n = len(list(numbers))
    max_product = 0
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    max_product = max1 * max2
    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))