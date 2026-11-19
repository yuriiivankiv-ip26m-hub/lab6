def calculate_discount(price, discount):
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise TypeError("Price must be a number")

    if not isinstance(discount, (int, float)) or isinstance(discount, bool):
        raise TypeError("Discount must be a number")

    if price < 0:
        raise ValueError("Price cannot be negative")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100")

    return round(price * (1 - discount / 100), 2)


if __name__ == "__main__":
    print(calculate_discount(1000, 15))