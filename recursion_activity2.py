def find_max(arr):
    # Input rule documented: requires a nonempty array
    if len(arr) == 0:
        raise ValueError("Array must contain at least one number.")
    
    # Base case: only one element left
    if len(arr) == 1:
        return arr[0]
    
    # Recursive step: compare current element with max of the rest
    max_of_rest = find_max(arr[1:])
    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest

# Tests
print("\n--- Find Max Tests ---")
print(find_max([42]))                   # Expected: 42 (one-number array)
print(find_max([10, 5, 2, 1]))          # Expected: 10 (largest at beginning)
print(find_max([1, 5, 2, 10]))          # Expected: 10 (largest at end)
print(find_max([-5, -2, -10, -8]))      # Expected: -2 (all negative numbers)
try:
    find_max([])
except ValueError as e:
    print(f"Empty array test: {e}")