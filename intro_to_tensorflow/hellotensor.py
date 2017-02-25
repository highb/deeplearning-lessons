import tensorflow as tf

# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)

x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
    print(output)

x = tf.add(5, 2)  # 7
x = tf.subtract(10, 4) # 6
y = tf.multiply(2, 5)  # 10

# casting
tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))   # 1

# TODO: Convert the following to TensorFlow:
x = tf.constant(10.)
y = tf.constant(2.)
z = tf.subtract(tf.divide(x, y), tf.constant(1.))

# TODO: Print z from a session
with tf.Session() as sess:
    output = sess.run(z)
print(output)
