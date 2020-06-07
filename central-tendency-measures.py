n = int(input())
arrayInput = input().split(" ")
arrayElements = [int(i) for i in arrayInput]

def mean():
    sum1 = 0
    for i in arrayElements:
        sum1 += i
    mean = round((sum1/n), 1)
    print(mean)
    
def median():
    (arrayElements).sort()
    if (len(arrayElements) % 2 != 0):
        median = arrayElements[int((len(arrayElements)-1)/2)]
    else:
        median = (arrayElements[int(len(arrayElements)/2)] + arrayElements[int(len(arrayElements)/2) - 1])/2
    print(median)    

def mode():
    arrayElements.sort()
    occCount = [arrayElements.count(i) for i in arrayElements]
    mode = arrayElements[occCount.index(max(occCount))]
    print (mode)

def main():
    mean()
    median()
    mode()

if __name__ == "__main__":
    main()
