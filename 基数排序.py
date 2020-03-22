def radix_sort(array):
    i = 0
    n = 1
    max_num = max(array)
    while max_num >= 10 ** n: n += 1
    while i < n:
        bucket = {}
        for _ in range(10): bucket[_] = []
        for item in array: bucket[item//(10 ** i) % 10].append(item)
        counter = 0
        for _ in range(10):
            if len(bucket[_]) != 0:
                for item in bucket[_]:
                    array[counter] = item
                    counter += 1
        i += 1

if __name__ == '__main__':
    a = [12,3,45,3543,214,1,4553]
    print("Before sorting...")
    print("---------------------------------------------------------------")
    print(a)
    print("---------------------------------------------------------------")
    radix_sort(a)
    print("After sorting...")
    print("---------------------------------------------------------------")
    print(a)
    print("---------------------------------------------------------------")

        
