def fibonacci_dp(n):
    if n < 0:
        return "Invalid input"
    
    # Khởi tạo mảng lưu trữ các giá trị Fibonacci đã tính
    fib = [0] * (n + 1)
    
    # Giá trị cơ sở
    if n > 0:
        fib[1] = 1
    
    # Tính Fibonacci bằng phương pháp quy hoạch động
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Nhập số n từ người dùng
n = int(input("Nhập số n: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci_dp(n)}")