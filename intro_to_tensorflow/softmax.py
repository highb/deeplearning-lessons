import tensorflow as tf

def run():
    output = None
    logit_data = [2.0, 1.0, 0.1]
    logits = tf.placeholder(tf.float32)
    softmax = tf.nn.softmax(logits)

    # TODO: Calculate the softmax of the logits
    # softmax =

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # TODO: Feed in the logit data
        output = sess.run(softmax, feed_dict={logits: logit_data})

    return output
