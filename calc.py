def add(a, b):
       # BUG: This should be addition, not multiplication
       return a * b

if __name__ == "__main__":
       result = add(2, 3)
       assert result == 5, f"Expected 5, but got {result}"
       print("All tests passed!")
