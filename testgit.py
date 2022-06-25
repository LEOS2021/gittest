import time
from itertools import product
start_time = time.time()
combo = (9, 9, 7, 6, 5, 4, 3, 2, 1)
# применить декартово произведение для генерирования перестановок
# с повтором
for perm in product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=len(combo)):
    if perm == combo:
        print("Взломано! {} {}".format(combo, perm))
        end_time = time.time()
        print("Время выполнения этой программы составило {} секунд." .format(
            end_time - start_time))
