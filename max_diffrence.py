def maximize_sublist_difference(nums):
    """
    Maximizes the difference between the sums of two sublists from a given list of integers.

    Args:
        nums (list): The list of integers.

    Returns:
        tuple: A tuple containing sublist A, sublist B, and the difference between their sums.

    Time Complexity: O(n log n), where n is the length of the input list.

    This function sorts the input list of integers, divides it into two sublists, and then calculates
    the difference between the sums of these sublists. By sorting the list first, the function ensures
    that the sublists have balanced sums, maximizing the difference between them.
    """
    # Sort the list of integers
    sorted_nums = sorted(nums)

    # Initialize two sublists
    sublist_A = []
    sublist_B = []
    n = len(sorted_nums)

    # Divide the sorted list into two sublists
    for i in range(int(n / 2)):
        sublist_A.append(sorted_nums[i])
    for i in range(int(n / 2), n):
        sublist_B.append(sorted_nums[i])

    # Calculate the difference between the sums of the sublists
    difference = abs(sum(sublist_A) - sum(sublist_B))

    return sublist_A, sublist_B, difference


# Example usage:
nums = [5, 8, 2, 10, 3, 6]
sublist_A, sublist_B, difference = maximize_sublist_difference(nums)
print("Sublist A:", sublist_A)
print("Sublist B:", sublist_B)
print("Difference:", difference)
