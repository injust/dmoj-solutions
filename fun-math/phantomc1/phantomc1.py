print(lambda p:" ".join(([p.__setitem__(j,0)for j in p[i*i::i]],`i`+"*"*(p[i-2]|p[i+2]>1))[1]for i in p[2:]if p[i]))(range(input()))