# image-compression-using-svd
**Project Summary: Image Compression Using Singular Value Decomposition (SVD)**

### Introduction
Image compression is an essential technique in digital image processing, aiming to reduce the storage and transmission cost while preserving the quality of images. One effective method for image compression is Singular Value Decomposition (SVD), which decomposes an image into a set of singular values that can be truncated to achieve compression. This project implements SVD-based image compression and evaluates its efficiency by analyzing transmission size reduction and error metrics.

### Methodology

#### **1. Image Loading and Preprocessing**
- The input image is read using OpenCV (`cv2.imread`) and converted from BGR to RGB format to ensure correct color representation.
- The pixel values are normalized to the range [0,1] by dividing by 255.0.
- The image is decomposed into its three color channels: Red (R), Green (G), and Blue (B).

#### **2. Singular Value Decomposition (SVD)**
- Each channel of the image undergoes SVD, which decomposes the matrix into three components:
  
  \[ A = U \Sigma V^T \]
  
  where:
  - `U` and `V^T` are orthonormal matrices.
  - `Σ` is a diagonal matrix containing singular values in descending order.
  
- The compression is achieved by truncating the matrices to keep only the top **k** singular values and corresponding vectors.

#### **3. Image Reconstruction**
- A compressed version of each channel is reconstructed using only the top **k** singular values:

  \[ A_k = U_k \Sigma_k V_k^T \]
  
- The reconstructed R, G, and B channels are stacked together to form the compressed image.

#### **4. Compression Evaluation**
- Different values of **k** are used to reconstruct the image to analyze the trade-off between compression ratio and image quality.
- The original image and compressed images are displayed for visual comparison.

#### **5. Storage and Transmission Size Analysis**
- The original storage size and compressed storage size are calculated using the formula:

  \[ Original Size = 3 \times r \times r \]
  \[ Compressed Size = 3 \times (r \times k + k + k \times r) \]
  
  where **r** is the number of rows (height of the image) and **k** is the number of singular values retained.

#### **6. Error Metrics Calculation**
To measure the quality of the compressed image, two error metrics are used:
- **2-Norm Error**: Measures the Euclidean distance between the original and compressed image matrices.
- **Frobenius Norm Error**: Computes the overall reconstruction error across the entire matrix.

### Results and Observations
- As **k** increases, the compressed image quality improves, but the storage requirement also increases.
- A small value of **k** (e.g., **k=5 or 20**) results in significant compression but with noticeable loss of detail.
- Higher values of **k** (e.g., **k=100 or 200**) provide visually appealing images with minimal loss while still reducing storage size compared to the original.
- The error metrics confirm that higher values of **k** reduce reconstruction errors, making the compressed image closer to the original.

### Conclusion
This project demonstrates the effectiveness of SVD in image compression by reducing storage requirements while preserving perceptual image quality. The ability to balance compression and quality by adjusting **k** makes SVD a powerful tool for various applications in image storage and transmission.

### Future Enhancements
- Implement adaptive **k** selection based on image complexity.
- Compare SVD with other compression techniques like JPEG and Principal Component Analysis (PCA).
- Explore real-time image compression for streaming applications.

This project highlights how mathematical decomposition techniques can efficiently compress images while retaining essential visual information.

