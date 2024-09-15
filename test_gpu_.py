'''
import torch
import pytorch_lightning as pl
print(torch.__version__)
print(pl.__version__)
'''

import os
#print(f"MASTER_ADDR: {os.getenv('MASTER_ADDR')}")
#print(f"MASTER_PORT: {os.getenv('MASTER_PORT')}")

print(os.cpu_count())