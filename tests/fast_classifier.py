import numpy as np
class fast_classifier(object):
    def __init__(self):
        pass

    def train(self, features, labels):
        examples = {}
        for f,lab in zip(features, labels):
            if lab not in examples:
                examples[lab] = f
        return fast_model(examples)

class fast_model(object):
    def __init__(self, examples):
        self.examples = examples
        assert len(self.examples)

    def apply(self, f):
        best = None
        best_val = +np.inf
        for k,v in self.examples.iteritems():
            dist = np.dot(v-f, v-f)
            if dist < best_val:
                best = k
                best_val = dist
        return best


