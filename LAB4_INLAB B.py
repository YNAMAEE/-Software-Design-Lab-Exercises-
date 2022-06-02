def MULTIPLY(M,N):

    if N==0:
        return 0
    else:
        return M+MULTIPLY(M,N-1)
    
print(MULTIPLY(54,45))
