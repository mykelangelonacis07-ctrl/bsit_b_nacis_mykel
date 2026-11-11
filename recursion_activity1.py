def sum_array(arr):
    # Base case: empty array
    if len(arr) == 0:
        return 0
    # Recursive step: first element + sum of the rest
    return arr[0] + sum_array(arr[1:])

# Tests
print("--- Sum Tests ---")
print(sum_array([]))                   # Expected: 0
print(sum_array([5]))                  # Expected: 5
print(sum_array([1, 2, 3, 4, 5]))      # Expected: 15
print(sum_array([10, -5, 3, -2]))      # Expected: 6
