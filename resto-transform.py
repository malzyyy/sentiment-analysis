
import tensorflow as tf

LABEL = "label"
SENTENCE = "sentence"

def transformed_name(key):
    return key + "_xf"

def preprocessing_fn(inputs):
    outputs = {}
    outputs[transformed_name(SENTENCE)] = tf.strings.lower(inputs[SENTENCE])
    outputs[transformed_name(LABEL)] = tf.cast(inputs[LABEL], tf.int64)
    return outputs
