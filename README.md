# CV_Project
Shadow Detection & Removal from Images

## How to Run?
- Install **Python 3.10** (if not 3.10 ensure 3.8 atleast)
- Go to desired ipynb file, for eg. **final.ipynb**
- Run all cells

## How to modify Hyperparameters?
In the Shadow Remover class all the hyperparameters used in the three techniques provided are taken as input while we're initializing the class.

```ruby
class ShadowRemover:
        itr: # Number of Iterations the algorithm will run
        method: # Technique to be used for mask calculation
        lab_adjustment: # Boolean for using Lab Adjustment for removal
        ab_threshold: # The AB-Threshold for Binarization during mask calculation
        region_adjustment_kernel_size: # Region Adjustment kernel used for Shadow Removal
        shadow_dilation_kernel_size: # Kernel size for highlighting shadows while removal
        shadow_dilation_iteration: # Number of Iterations for Shadow Dilation
        shadow_size_threshold: # The Threshold for detecting shadow sizes
        verbose: # For displaying every region in every iterations
        plot_results: # For displaying the results in plot
```

## Directory Structure
- **Experiments** - All things we tried
  - colour_adjustment.py - Can modify pixel colours
  - model.ipynb - For running the DL Model
  - scanned_documents.ipynb - Shadow Removal on Scanned Documents
  - trained_model4.pth - Trained model weights
- **Images** - Folder for images
- **Results** - Result Images
- **final.ipynb** - Final ipynb file containing the code of our final implementation


## Contributors
| Name                                            | Year      | Department                       |
| ----------------------------------------------- | --------- | -------------------------------- |
| Anadi Sharma | B21CS008 | Computer Science and Engineering |
| Drishti Agrawal | B21CS027 | Computer Science and Engineering |
| Shubh Goyal | B21CS073 | Computer Science and Engineering |
| Sukriti Goyal | B21CS075 | Computer Science and Engineering |
