

def findShortestString(arr):
  
    # array_of_length = [len(e) for e in arr]

    # min_len = min(array_of_length)
    # index = array_of_length.index(min_len)
    # res = arr[index]

    # return res
    shortest = arr[0]

    for s in arr:
        if len(s) < len(shortest):
            shortest = s

    return shortest




