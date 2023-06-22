
# class EvaluationNetConvMaxPool(nn.Module):
#     def __init__(self, input_dim=40, input_channels=1):
#         super(EvaluationNetConvMaxPool, self).__init__()
#         self.conv1 = nn.Conv2d(input_channels, 30, kernel_size=5, stride=1, padding=0)
#         self.conv2 = nn.Conv2d(30, 60, kernel_size=5, stride=1, padding=0)
#         #self.fc1 = nn.Linear(30 * (input_dim // 4) ** 2, 1000)
#         self.fc1 = nn.Linear(2940, 1000)
#         # self.fc2 = nn.Linear(1000, 4)
#         self.fc_value = nn.Linear(1000, 1)  # new linear layer to output the value estimate
#
#     def forward(self, x):
#         x = F.relu(self.conv1(x))
#         x = F.max_pool2d(x, 2, 2)
#         x = F.relu(self.conv2(x))
#         x = F.max_pool2d(x, 2, 2)
#         x = x.view(x.size(0), -1)  # flatten the tensor
#         x = F.relu(self.fc1(x))
#         # action_probs = F.softmax(self.fc2(x), dim=1)  # apply softmax to output action probabilities
#         value_estimate = self.fc_value(x)
#         return value_estimate