
mnozhestvo = list(map(int, input("vvedite chisla cherez probel").split()))
chislo=int(input("vvedite chislo"))
def sortirovka(mnozhestvo):
    for i in range(len(mnozhestvo)):
        for j in range(len(mnozhestvo) - i - 1):
            if mnozhestvo[j] > mnozhestvo[j + 1]:
                mnozhestvo[j], mnozhestvo[j + 1] =mnozhestvo[j + 1], mnozhestvo[j]
    return mnozhestvo
print(sortirovka(mnozhestvo))


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

element = chislo
array = mnozhestvo
left=0
right=len(mnozhestvo)

index=binary_search(array, element, left, right)
if index == False:
    print("chislo ne naideno")
else:print(index-1)
