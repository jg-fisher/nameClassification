import torch
from torch import nn, optim
import torch.utils.data as data_utils
import torch.nn.functional as F
from preprocessing import process_data

# Seed for reproducibility
torch.manual_seed(12)

# Parameters
epochs = 100
batch_size = 20
learn_rate = .01
input_size = 36
num_classes = 3

# Data
X, Y, _ = process_data()

# Convert to tensor
X = torch.Tensor(X).float()
Y = torch.Tensor(Y).long()

# Initialize data loader
dataset = data_utils.TensorDataset(X, Y)
data_loader = data_utils.DataLoader(dataset, batch_size=batch_size)

# Network 
class Classifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.h1 = nn.Linear(input_size, 100)
        self.h2 = nn.Linear(100, 50)
        self.h3 = nn.Linear(50, num_classes)
    
    def forward(self, x):
        x = self.h1(x)
        x = F.relu(x)
        x = self.h2(x)
        x = F.relu(x)
        x = F.softmax(x, dim=1)
        return x

if __name__ == '__main__':
    # Network instance and optimizer
    model = Classifier(input_size, num_classes)
    opt = optim.Adam(params=model.parameters(), lr=learn_rate)
    
    #criterion = nn.MultiLabelSoftMarginLoss()
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        for n_batch, batch in enumerate(data_loader, 0):
    
            x, y = batch
            output = model(x)
            loss = criterion(output, y)
    
            print("Loss: {}".format(loss))
    
            model.zero_grad()
            loss.backward()
            opt.step()
    
            #_, pred = output.max(1)
    
    torch.save(model.state_dict(), 'weights.pth')
    
        
