for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            product_abc = a * b * c
            print(f"The Pythagorean : a = {a}, b = {b}, c = {c}")
            print(f"abc : {product_abc}")
            break
