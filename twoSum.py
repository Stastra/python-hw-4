""" Створіть функцію def twoSum(nums, target) яка приймає цілочисельний масив, і ціле число, 
а повертає індекси двох чисел массиву так, щоб їх сума дала передане ціле число.

Ви можете припустити, що кожен вхід матиме рівно одне рішення,
Ви не можете використовувати той самий елемент двічі.

Ви можете повернути відповідь у будь-якому порядку.

Приклади:

twoSum([1, 2, 3], 4) -> [0, 2]
twoSum([2, 7, 11, 15], 9) -> [0, 1]
twoSum([3, 2, 4], 6) -> [1, 2]
twoSum([3, 3], 6) -> [0, 1] """


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for x in range(len(nums)):
        for y in range(len(nums)):
            if nums[x] + nums[y] == target and x != y:
                return [x,y]



print(twoSum([1, 2, 3], 4))        # [0, 2]
print(twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(twoSum([3, 2, 4], 6))        # [1, 2]
print(twoSum([3, 3], 6))           # [0, 1]

