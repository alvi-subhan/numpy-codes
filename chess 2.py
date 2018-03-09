import numpy as np
b=np.ones(64,dtype="uint32").reshape(8,8)
b[:,1::2]=0
print(b)