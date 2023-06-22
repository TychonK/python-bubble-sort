import random

from timeit import default_timer as timer

# creating random array

def generate_random_array(size, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(size)]

size = 12
minimum = 1
maximum = 100

randomArray = generate_random_array(size, minimum, maximum)
print('Intial array with no order: ' + str(randomArray))

# bubble sorting the array

def bubbleSort(arr):
  
  for i in range(len(arr)):

    for j in range(0, len(arr) - i - 1):

      if arr[j] > arr[j + 1]:

        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp

# set timer

start = timer()

# execute sort function
bubbleSort(randomArray)

end = timer()

print('Sorted array in ascending order: ' + str(randomArray))

print('Time required to execute the sorting: ' + str(end - start))