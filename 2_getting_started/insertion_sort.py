from array import array

def insertion_sort(ary):
    for j in range(1, len(ary)):
        key = ary[j]
        i = j - 1
        while i > -1 and ary[i] > key:
            ary[i+1] = ary[i]
            i = i - 1
        ary[i+1] = key
    return ary

if __name__ == '__main__':
    ary = array('i', [3, 7, 2, 1, 10])
    print(ary, "\n")
    assert insertion_sort(ary) == array('i', [1, 2, 3, 7, 10])
    print(insertion_sort(ary), "\n")
