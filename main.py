"""
    U vsech algo kopiruji pole, to do prostorove slozitosti nepocitam (normalne neni potreba)
    Vsechny algoritmy (az na ty nejlehci) jsou z geekforgeeks.org
"""
import time
import random


def bubble_sort(input_list) -> []:
    """
        stabilní řadící algoritmus
        Asi nejjednodusi na implementaci
        Prohazuje vzdy dva sousedni prvky

        Worst Case Time Complexity [ Big-O ]: O(n2)
        Best Case Time Complexity [Big-omega]: O(n) (kdyz uz je pole serazeno)
        Average Time Complexity [Big-theta]: O(n2)
        Space Complexity: O(1) - potrebuje jedno misto pro tmp
        https://stackabuse.s3.amazonaws.com/media/bubble-sort-in-java-1.gif
    """
    arr = input_list.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    return arr


def insertion_sort(input_list) -> []:
    """
        stabilní řadící algoritmus
        Neco jako bubble sort, ale prohazuje cislo radi hned na spravne misto (prohazuje vlastne cele pole)
        Efektivni pro maly objem dat, velmi neefektivni pro velko objem dat
        Lepsi nez bubble nebo selection sort

        Worst Case Time Complexity [ Big-O ]: O(n2)
        Best Case Time Complexity [Big-omega]: O(n)
        Average Time Complexity [Big-theta]: O(n2)
        Space Complexity: O(1)
        http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/images/bubble1.gif
    """
    arr = input_list.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def selection_sort(input_list) -> []:
    """
        nestabilni radici algoritmus
        rychlejsi nez bubble pomalejsi nez insert
        hleda nejvetsi/nejmensis prvky ze zbyvajiciho neserazeneho pole a ty radi

        Worst Case Time Complexity [ Big-O ]: O(n2)
        Best Case Time Complexity [Big-omega]: O(n2)
        Average Time Complexity [Big-theta]: O(n2)
        Space Complexity: O(1)
        https://gfycat.com/snappymasculineamericancicada
    """

    arr = input_list.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        tmp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = tmp

    return arr


def partition(arr, low, high):
    """ For quicksort """
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high) -> []:
    """
        rychly nestabilni algoritmus
        pivot - nejlepe prostredni prvek (podle velikosti) - mensi cisla | pivot | vetsi cisla

        Worst Case Time Complexity [ Big-O ]: O(n2)
        Best Case Time Complexity [Big-omega]: O(n*log n)
        Average Time Complexity [Big-theta]: O(n*log n)
        Space Complexity: O(n*log n)
        https://www.tutorialspoint.com/data_structures_algorithms/images/quick_sort_partition_animation.gif
    """

    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def merge_sort(arr) -> []:
    """
        stabilni algoritmus
        rozdeli na mensi casti, ty seradi a potom spoji +-

        Worst Case Time Complexity [ Big-O ]: O(n*log n)
        Best Case Time Complexity [Big-omega]: O(n*log n)
        Average Time Complexity [Big-theta]: O(n*log n)
        Space Complexity: O(n)
        http://www-scf.usc.edu/~zhan468/public/Notes/resources/CDDA3F11C6EFBC01577F5C29A9066772.gif
    """

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    """
        nestabilni algoritmus
        jeden z nejlepsi algoritmu na razeni
        popr. muze nekdo doplnit info :D

        Worst Case Time Complexity: O(n*log n)
        Best Case Time Complexity: O(n*log n)
        Average Time Complexity: O(n*log n)
        Space Complexity : O(1)
    """

    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def create_unsorted_array(len) -> []:
    arr = []
    for i in range(len):
        arr.append(random.randint(1, 10000))
    return arr



if __name__ == '__main__':

    base_arr = create_unsorted_array(10000)
    printArray = False

    print("Bubble sort: ")
    t0 = time.time()
    arr = bubble_sort(base_arr)
    if printArray: print(arr)
    t1 = time.time() - t0
    print("Time elapsed: ", "%.14f" % t1)

    print("Insertion sort")
    t0 = time.time()
    arr = insertion_sort(base_arr)
    if printArray: print(arr)
    t1 = time.time() - t0
    print("Time elapsed: ", "%.14f" % t1)

    print("Selection sort")
    t0 = time.time()
    arr = selection_sort(base_arr)
    if printArray: print(arr)
    t1 = time.time() - t0
    print("Time elapsed: ", "%.14f" % t1)

    """ Rekurzivni algo: """

    print("Quick sort")
    arr = base_arr.copy()
    t0 = time.time()
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    if printArray: print(arr)
    t1 = time.time() - t0
    print("Time elapsed: ", "%.14f" % t1)

    print("Merge sort")
    arr = base_arr.copy()
    t0 = time.time()
    merge_sort(arr)
    if printArray: print(arr)
    t1 = time.time() - t0
    print("Time elapsed: ", "%.14f" % t1)

    print("Heap sort")
    arr = base_arr.copy()
    t0 = time.time()
    heap_sort(arr)
    if printArray: print(arr)
    t1 = time.time() - t0
    print("Time elapsed: ", "%.14f" % t1)
