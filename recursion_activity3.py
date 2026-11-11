def count_target(arr, target):
    # Base case: no numbers left to examine
    if len(arr) == 0:
        return 0
    
    # Check if current number matches the target
    if arr[0] == target:
        match = 1
    else:
        match = 0
        
    # Recursive step: current match + count in the rest of the array
    return match + count_target(arr[1:], target)

# Tests
print("\n--- Count Target Tests ---")
print(count_target([], 5))                      # Expected: 0 (empty array)
print(count_target([1, 2, 3, 2, 4, 2], 2))      # Expected: 3 (appears several times)
print(count_target([1, 2, 3, 4, 5], 9))         # Expected: 0 (does not appear)