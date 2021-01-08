""" U vsech algo kopiruji pole, to do prostorove slozitosti nepocitam (normalne neni potreba) """


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


if __name__ == '__main__':
    arr = [10, 40, 2, 12, 98, 30, 22, 12]
    print("Bubble sort: ")
    print(bubble_sort(arr))

    print("Insertion sort")
    print(insertion_sort(arr))

    print("Selection sort")
    print(selection_sort(arr))
