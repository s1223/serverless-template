import tensorflow as tf

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    pass

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    # Parse out your arguments
    prompt = model_inputs.get('url', None)
    if prompt == None:
        return {'message': "No url provided"}
    
    # Run the model
    physical_devices = tf.config.list_physical_devices('GPU')
    result = f"Number of GPU : {len(physical_devices)}"

    # Return the results as a dictionary
    return result
