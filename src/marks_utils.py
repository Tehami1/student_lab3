
import numpy as np

def standardise_loop(data):
    data = np.asarray(data, dtype=float)
    rows, cols = data.shape

    means = []
    stds = []

    for j in range(cols):
        column = [data[i, j] for i in range(rows)]
        mean = sum(column) / rows
        variance = sum((x - mean) ** 2 for x in column) / rows
        means.append(mean)
        stds.append(variance ** 0.5)

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            if stds[j] == 0:
                row.append(0.0)
            else:
                row.append((data[i, j] - means[j]) / stds[j])
        result.append(row)

    return np.array(result)


def standardise_np(data):
    data = np.asarray(data, dtype=float)
    means = data.mean(axis=0)
    stds = data.std(axis=0)
    stds[stds == 0] = 1.0
    return (data - means) / stds
