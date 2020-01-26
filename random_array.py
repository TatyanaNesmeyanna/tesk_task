import random
from collections import Counter


my_array=[random.randint(0, 10) for _ in range(100)]
# method 1
counts = Counter(my_array)

# method 2
counts_2 = {}
for x in my_array:
    counts_2[x] = counts_2[x]+1 if x in counts_2 else 1

print(my_array)
print(counts)
print(counts_2)