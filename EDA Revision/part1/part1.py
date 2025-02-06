import numpy as np

def calculate(num):
    if len(num) != 9:
         raise ValueError("List must contain nine numbers.")

    matrix = np.array(num).reshape(3,3)

    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return calculations

num = list(map(int, input("Enter 9 numbers separated by spaces: ").split()))
result = calculate(num)


for key, value in result.items():
    print(f"{key}:")
    print(value, "\n")
