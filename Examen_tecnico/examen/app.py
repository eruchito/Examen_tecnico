def puede_formarse(nums, requiredSum):
    elementos_vistos = set()
    
    for num in nums:
        complemento = requiredSum - num
        if complemento in elementos_vistos:
            return True
        elementos_vistos.add(num)
    return False

nums1 = [1, 4, 3, 9]
requiredSum1 = 8
print(f"Input: nums = {nums1}, requiredSum = {requiredSum1}")
print(f"Output: {puede_formarse(nums1, requiredSum1)}") 

nums2 = [1, 2, 4, 4]
requiredSum2 = 8
print(f"\nInput: nums = {nums2}, requiredSum = {requiredSum2}")
print(f"Output: {puede_formarse(nums2, requiredSum2)}")  
