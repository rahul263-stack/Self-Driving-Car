import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# Create TensorFlow object tensor
hello_constant = tf.constant('Hello World!')
# Print hello world in TensorFlow 
with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)
