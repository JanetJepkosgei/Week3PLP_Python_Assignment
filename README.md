# Discount Calculator Function

This program defines a function named `calculate_discount(price, discount_percent)` that calculates the final price after applying a discount.  

If the discount is **20% or higher**, the discount is applied. Otherwise, the function returns the original price.


## Function Definition

```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 0.20:
        return price - (price * discount_percent)
    else:
        return price
```

# Example test cases
```output
print(calculate_discount(100, 0.20))   # 80.0 (20% discount applied)
print(calculate_discount(18000, 0.10)) # 18000 (No discount applied)
print(calculate_discount(100, 0.80))   # 20.0 (80% discount applied)
```
