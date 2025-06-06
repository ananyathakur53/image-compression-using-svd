# -*- coding: utf-8 -*-
"""Image_compression_using_SVD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aRzDmAMY3gRic27AxyUO09BsPQ8NQQe2
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
image = cv2.imread(r'/content/tmp_5897889b-1501-48b0-83fc-5657e98437de.png')

if image is None:
    print("Error: Image not loaded. Check the file path and format.")
else:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


image = image / 255.0

R, G, B = cv2.split(image)

def svd_compress(channel, k):
    U, Sigma, VT = np.linalg.svd(channel, full_matrices=False)
    Sigma_k = np.diag(Sigma[:k])
    U_k = U[:, :k]
    VT_k = VT[:k, :]
    return np.dot(U_k, np.dot(Sigma_k, VT_k)), Sigma  # Return the compressed channel and singular values


k_values = [5, 20, 50, 100, 150, 200]

fig, axes = plt.subplots(1, len(k_values) + 1, figsize=(20, 10))
axes[0].imshow(image)
axes[0].set_title("Original Image")
axes[0].axis("off")


for i, k in enumerate(k_values):
    R_compressed, _ = svd_compress(R, k)
    G_compressed, _ = svd_compress(G, k)
    B_compressed, _ = svd_compress(B, k)

    compressed_image = np.stack([R_compressed, G_compressed, B_compressed], axis=2)
    axes[i + 1].imshow(np.clip(compressed_image, 0, 1))
    axes[i + 1].set_title(f"k = {k}")
    axes[i + 1].axis("off")

plt.show()
def calculate_transmission_size(r, k):
    original_size = 3 * r * r
    compressed_size = 3 * (r * k + k + k * r)
    return original_size, compressed_size


r = R.shape[0]

for k in k_values:
    original_size, compressed_size = calculate_transmission_size(r, k)
    print(f"For k = {k}, original size: {original_size} entries, compressed size: {compressed_size} entries")

def calculate_errors(original_channel, compressed_channel):
    original_flatten = original_channel.flatten()  # Flatten the original channel
    compressed_flatten = compressed_channel.flatten()  # Flatten the compressed channel

    two_norm_error = np.linalg.norm(original_flatten - compressed_flatten, ord=2)
    frobenius_norm_error = np.linalg.norm(original_channel - compressed_channel, ord='fro')  # Frobenius norm should be computed on the full matrix

    return two_norm_error, frobenius_norm_error



for k in k_values:
    R_compressed, Sigma_R = svd_compress(R, k)
    G_compressed, Sigma_G = svd_compress(G, k)
    B_compressed, Sigma_B = svd_compress(B, k)

    compressed_image = np.stack([R_compressed, G_compressed, B_compressed], axis=2)

    R_2_norm, R_fro_norm = calculate_errors(R, R_compressed)
    G_2_norm, G_fro_norm = calculate_errors(G, G_compressed)
    B_2_norm, B_fro_norm = calculate_errors(B, B_compressed)

    avg_2_norm = (R_2_norm + G_2_norm + B_2_norm) / 3
    avg_fro_norm = (R_fro_norm + G_fro_norm + B_fro_norm) / 3

    print(f"For k = {k}: 2-Norm Error = {avg_2_norm}, Frobenius Norm Error = {avg_fro_norm}")