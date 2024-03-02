def sort_on(arr, k):
    """
    Sorts an array containing integers within a limited range using counting sort_sudo.

    Args:
        arr (list): The input array to be sorted.
        k (int): The constant multiplier to determine the range of integers.

    Returns:
        list: The sorted array.

    Time Complexity: O(n + int_range), where n is the length of the input array and
                    int_range is proportional to n * k.

    This function sorts the input array in ascending order by first counting the occurrences
    of each integer within the specified range, then reconstructing the sorted array based on
    the counts of occurrences.
    """
    n = len(arr)  # Length of input array
    int_range = k * n + 1  # Define the range of integers to be encountered

    # Initialize count array to keep track of whether each integer in the range exists in the input array
    count = []
    for i in range(0, int_range):
        count+=[0]

    # Mark each integer that exists in the input array
    for num in arr:
        count[num] = 1

    # Reconstruct sorted array from the marked integers
    sorted_arr = []
    for i in range(1, int_range):
        if count[i] == 1:
            sorted_arr+=[i]

    return sorted_arr


# Example usage:
arr = [5, 30, 7, 2, 80, 6, 1, 4]
n = len(arr)
k = 10
int_range = k * n
sorted_arr = sort_on(arr, k)
print(f" k = {k} \n n = {n} \n int_range = (1,{int_range}) \n array={arr} \n sorted_array {sorted_arr}")
