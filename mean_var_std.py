import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list)
    arr = arr.reshape(3, 3)

    #mean
    mean_1 = np.mean(arr, axis=0)
    mean_2 = np.mean(arr, axis=1)
    mean_3 = np.mean(arr)

    mean_1 = mean_1.tolist()
    mean_2 = mean_2.tolist()
    mean_3 = mean_3.tolist()
    mean_list = [mean_1, mean_2, mean_3]

    #variance
    var_1 = np.var(arr, axis=0)
    var_2 = np.var(arr, axis=1)
    var_3 = np.var(arr)

    var_1 = var_1.tolist()
    var_2 = var_2.tolist()
    var_3 = var_3.tolist()
    var_list = [var_1, var_2, var_3]

    #standard deviation
    std_1 = np.std(arr, axis=0)
    std_2 = np.std(arr, axis=1)
    std_3 = np.std(arr)

    std_1 = std_1.tolist()
    std_2 = std_2.tolist()
    std_3 = std_3.tolist()
    std_list = [std_1, std_2, std_3]

    #max
    max_1 = np.max(arr, axis=0)
    max_2 = np.max(arr, axis=1)
    max_3 = np.max(arr)

    max_1 = max_1.tolist()
    max_2 = max_2.tolist()
    max_3 = max_3.tolist()
    max_list = [max_1, max_2, max_3]

    # min
    min_1 = np.min(arr, axis=0)
    min_2 = np.min(arr, axis=1)
    min_3 = np.min(arr)

    min_1 = min_1.tolist()
    min_2 = min_2.tolist()
    min_3 = min_3.tolist()
    min_list = [min_1, min_2, min_3]

    # sum
    sum_1 = np.sum(arr, axis=0)
    sum_2 = np.sum(arr, axis=1)
    sum_3 = np.sum(arr)

    sum_1 = sum_1.tolist()
    sum_2 = sum_2.tolist()
    sum_3 = sum_3.tolist()
    sum_list = [sum_1, sum_2, sum_3]

    calculations = {
        "mean": mean_list,
        "variance": var_list,
        "standard deviation": std_list,
        "max": max_list,
        "min": min_list,
        "sum": sum_list
    }

    return calculations