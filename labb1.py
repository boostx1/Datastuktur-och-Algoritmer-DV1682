def linear_search(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

def insertionsort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def selectionsort(lst):
    #för varje index 
    for i in range (len(lst) - 1):
        #identifera minsta element
        minimum_index = i
        for j in range (i + 1, len(lst)):
            if lst[j] < lst[minimum_index]: 
                minimum_index = j
        
        #Byta plats på nuvarande (i) och minsta
        lst[i], lst[minimum_index] = lst[minimum_index], lst[i]

def binary_search(lst, element):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(lst, element):
    def helper(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            return helper(mid + 1, high)
        else:
            return helper(low, mid - 1)
    return helper(0, len(lst) - 1)

def insertionsort_with_binary_search(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]

        # Binärsök insättningsposition i [0, i)
        lo, hi = 0, i - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if a[mid] <= key:      # <= gör algoritmen stabil
                lo = mid + 1
            else:
                hi = mid - 1
        insert_pos = lo  # första plats där key ska in

        # Skjut elementen ett steg åt höger för att skapa plats
        j = i - 1
        while j >= insert_pos:
            a[j + 1] = a[j]  # EN assignment per förskjutning
            j -= 1

        # Lägg in key
        a[insert_pos] = key

    return a  # om CodeGrade kräver "in place" utan retur: ta bort denna rad


def linear_search_recursive(lst, element):
    def helper(index):
        if index >= len(lst):
            return -1
        if lst[index] == element:
            return index
        return helper(index + 1)
    return helper(0)
