import random
import timeit
import matplotlib.pyplot as plt
import pandas as pd

# сортування вставками
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Timsort
def timsort(arr):
    return sorted(arr)

# Вимірювання часу
def benchmark(sort_func, data):
    stmt = lambda: sort_func(data)
    return timeit.timeit(stmt, number=1)

# Розміри масивів
sizes = [100, 500, 1000, 2000, 5000]
results = []

for size in sizes:
    test_data = [random.randint(1, 10000) for _ in range(size)]
    result = {
        "Розмір масиву": size,
        "Insertion Sort (сек)": benchmark(insertion_sort, test_data),
        "Merge Sort (сек)": benchmark(merge_sort, test_data),
        "Timsort (сек)": benchmark(timsort, test_data),
    }
    results.append(result)

df = pd.DataFrame(results)
print(df)

plt.figure(figsize=(10, 6))
plt.plot(df["Розмір масиву"], df["Insertion Sort (сек)"], marker='o', label="Insertion Sort")
plt.plot(df["Розмір масиву"], df["Merge Sort (сек)"], marker='o', label="Merge Sort")
plt.plot(df["Розмір масиву"], df["Timsort (сек)"], marker='o', label="Timsort")
plt.title("Порівняння")
plt.xlabel("Розмір масиву")
plt.ylabel("Час (сек)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
