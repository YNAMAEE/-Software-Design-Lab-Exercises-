def recMin(DATA):
    if len(DATA)==0:
        return None
    if len(DATA)==1:
        return DATA[0]
    return min(DATA[0], recMin(DATA[1:]))
def recMax(DATA):
        if len(DATA)==0:
            return None
        if len(DATA)==1:
            return DATA[0]
        return max(DATA[0], recMax(DATA[1:]))
def recRev(DATA):
    if len(DATA)<=1:
        return DATA
    return recRev(DATA[1:])+[DATA[0]]
print(recMin([1,2,3,4,5,6]))
print(recMax([1,2,3,4,5,6]))
print(recRev([1,2,3,4,5,6]))