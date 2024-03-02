def minimize_sublist_difference(nums):
    """
    Minimizes the difference between the sums of two sublists from a given list of integers.

    Args:
        nums (list): The list of integers.

    Returns:
        tuple: A tuple containing sublist A, sublist B, and the difference between their sums.

    Time Complexity: O(n log n), where n is the length of the input list.

    This function first sorts the input list of integers in descending order, then iterates
    through the sorted list and assigns each integer to the sublist with the smaller sum.
    Finally, it calculates the difference between the sums of the two sublists.
    """
    # Sort the list of integers in descending order
    sorted_nums = reversed(sorted(nums))

    # Initialize two sublists
    sublist_A = []
    sublist_B = []

    # Iterate through the sorted list in reverse order
    for num in sorted_nums:
        # Add the current integer to the sublist with the smaller sum
        if sum(sublist_A) <= sum(sublist_B):
            sublist_A.append(num)
        else:
            sublist_B.append(num)

    # Calculate the difference between the sums of the sublists
    difference = abs(sum(sublist_A) - sum(sublist_B))

    return sublist_A, sublist_B, difference


# Example usage:
nums = [5, 8, 2, 10, 3, 6]
sublist_A, sublist_B, difference = minimize_sublist_difference(nums)
print("Sublist A:", sublist_A)
print("Sublist B:", sublist_B)
print("Difference:", difference)
