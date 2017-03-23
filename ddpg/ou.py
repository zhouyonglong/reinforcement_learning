import numpy as np


# class OUProcess(object):
#   """Ornstein-Uhlenbeck process"""


#   def __init__(self, action_size, mu=0, theta=0.15, sigma=0.3):
#     self.action_size = action_size
#     self.mu = mu
#     self.theta = theta
#     self.sigma = sigma
#     self.x = np.ones(self.action_size) * self.mu


#   def noise(self):
#     self.x = self.x + self.theta * (self.mu - self.x) + self.sigma * np.random.randn(len(self.x))
#     return self.x


class OUProcess(object):
  """Ornstein-Uhlenbeck process"""


  def __init__(self, x_size, mu=0, theta=0.15, sigma=0.3):
    self.x = np.ones(x_size) * mu
    self.x_size = x_size
    self.mu = mu
    self.theta = theta
    self.sigma = sigma


  def noise(self):
    dx = self.theta * (self.mu - self.x) + self.sigma * np.random.randn(self.x_size)
    self.x = self.x + dx
    return self.x



