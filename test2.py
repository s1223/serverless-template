import banana_dev as banana
import time

api_key = "f406053a-5d60-4e05-a8ff-b73596a6d493" # "YOUR_API_KEY"
model_key = "78c68dcd-3832-4c36-95a4-70388ac0005d" # "YOUR_MODEL_KEY"
model_inputs = {'url': 'Hello I am a [MASK] model.'}

startTime = time.time()
out = banana.run(api_key, model_key, model_inputs)
print(out)
endTime =  time.time()
print("Time: ", endTime - startTime)