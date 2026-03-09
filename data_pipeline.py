from functions import *
import time
import datetime

print('Starting data pipeline at ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('===================================================================')

#* step 1: extract video IDs
t0 = time.time()
getVideoIDs()
t1 = time.time()
print('Step 1: done')
print('--> Video IDs downloaded in', str(t1-t0), 'seconds', '\n')

#* step 2: extract transcript for videos
t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print('Step 2: done')
print('--> Transcripts downloaded in', str(t1-t0), 'seconds', '\n')

#* step 3: transform data
t0 = time.time()
transformData()
t1 = time.time()
print('Step 3: done')
print('--> Data transformed in', str(t1-t0), 'seconds', '\n')

#* step 4: generate text embeddings
t0 = time.time()
createTextEmbeddings()
t1 = time.time()
print('Step 4: done')
print('--> Embeddings generated in', str(t1-t0), 'seconds', '\n')