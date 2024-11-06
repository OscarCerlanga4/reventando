#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe


def my_generator(n):
    value = 0 # initialize counter
    while value < n:
        yield value  # produce current
        value += 1   # increment counter
        
if __name__ == "__main__":
        
    for item in my_generator(1000000000):
        print(item)