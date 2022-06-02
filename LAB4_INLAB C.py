def Reverse(String):
    if len(String) > 0:
        Reverse(String[1:])
        print(String[0],end='')
Reverse('POTS & PANS')