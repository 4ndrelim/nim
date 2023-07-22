from nim import train, play
import time
from config import epochs

start_time = time.time()
ai = train(epochs)
print(f"Train time: {time.time() - start_time}")
play(ai)
