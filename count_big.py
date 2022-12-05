import math
from timeit import default_timer as timer

start = timer()

i=0
while i <= 100000000:
    i+=1
end = timer()

runtime = math.ceil((end - start)*1e6)/1000
print('Time taken: ', runtime,'ms')