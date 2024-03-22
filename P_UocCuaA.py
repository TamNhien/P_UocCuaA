a = int(input("Nhập vào số nguyên dương a: "))
print("Các ước của", a, "là:", *[i for i in range(1, a + 1) if a % i == 0])

