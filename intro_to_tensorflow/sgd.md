## Stochastic Gradient Descent

Naive Gradient Descent calculates loss based on entire dataset, so it is computationally
expensive.

SGD makes an estimate of the loss by only calculating the loss on a random sample
of the data (this is what we have been doing so far) and then finds the derivative
for that loss to determine which direction to move the weight/bias optimization.

### Requirements
* Inputs with a mean as close to 0 as possible, and a equal/small variance.
* Initial weights/biases that fit a normal distribution (and thus a mean close to 0) and equal variance.

### Optimizations
* Momentum
  * Take a running average of the loss derivative and apply that to the optimization at each step. This should improve convergance.
* Learning rate decay
  * Tune the learning rate as training continues, based on the number of epochs so far, when the loss change plateaus, or some other criteria

### Hyper-parameter tuning
You can change many hyper-params:
* initial learning rate
* learning rate decay
* Momentum
* batch size
* weight initialization

ADAGRAD is a modified version of SGD that does learning rate and momentum.
