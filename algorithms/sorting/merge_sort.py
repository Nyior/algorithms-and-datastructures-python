"""
 The merge sort is another comparison based sorting algorithm. It adopts the devide
 and conquer approach to problem solving. It splits a list into sublists, sorts the
 sublist, and then merges them back.
 It has a running time of O(nlogn). It is not an in-place algorithm, though stable.
"""
 
def merge_sort(data):
        
    # Our base case would be when the original array has been split into sub arrays
    # containing just one element each. An array containing just one element is definitely ordered
    if len(data) == 1:
        return

    # DEVIDE PHASE: This is where we keep splitting the array until the base case is hit.
    midpoint = len(data)//2
    left_subarray = data[:midpoint]
    right_subarray = data[midpoint:]

    # Recursively split the array to smaller arrays
    merge_sort(left_subarray)
    merge_sort(right_subarray)

    # CONQUER PHASE: this where we merge the sub arrays into a single new array.
    # We do this, by comparing each array element with each other and merging them 
    # into a result array we will create
    i = 0 # track elems in left subarray
    j = 0 # track elements in right sub array
    k = 0 # manipulate result array
    
    left_length = len(left_subarray)
    right_length = len(right_subarray)
    
    while i < left_length and j < right_length:
        item_1 = left_subarray[i]
        item_2 = right_subarray[j]
        
        if item_1 <= item_2:
            data[k] = item_1
            i += 1

        else:
            data[k] = item_2
            j += 1
        k += 1

    # If there are still items in the left subarray
    while i < left_length:
        data[k] = left_subarray[i]
        i += 1
        k += 1

    # If there are still items in the rightt subarray
    while j < right_length:
        data[k] = right_subarray[j]
        j += 1
        k += 1
   
# TODO: revise all sorting algorithms, Understand recursion and the stack memory, practice hackerrank sorting probs