def calculate_discount(price, discount_percent):
    if discount_percent >= 0.20:  # Check if discount is 20% or more
        return price - (price * discount_percent)  # Apply discount
    else:
        return price  # Return original price if discount < 20%

# Testing the function
print(calculate_discount(100, 0.20))    # 80.0
print(calculate_discount(18000, 0.10))  # 18000 (no discount applied)
print(calculate_discount(100, 0.80))    # 20.0
