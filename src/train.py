import torch
import sys

def sanity_check():
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"PyTorch Version: {torch.__version__}")

    # Create a random tensor (matrix)
    x = torch.rand(5, 3)
    print("\nSUCCESS! PyTorch is alive. Here is a random tensor:")
    print(x)

if __name__ == "__main__":
    sanity_check()