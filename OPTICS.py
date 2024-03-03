# -*- coding: utf-8 -*-
"""Code - Nhom07

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UxxXBq0kRouj_YnJKRJmrZm23WX-AqFf
"""

# Đặt seed để cố định tập data khi sinh ra
random_seed = 999

import random
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import OPTICS
from sklearn.datasets import make_moons
import numpy as np
import pandas as pd

"""# SET 1"""

def generate_data(num_points, seed=999):
    data = []
    noise_interval = 10  # Mỗi 10 điểm có một điểm nhiễu

    # Tạo random seed cho tái sử dụng
    random.seed(seed)
    np.random.seed(seed)

    # Tạo trung tâm cụm
    center1 = (4, 4)
    center2 = (8, 8)

    for i in range(num_points):
        # Chia dãy thành 2 cụm và xác định trung tâm tương ứng
        if i < num_points // 2:
            center = center1
        else:
            center = center2

        # Tạo nhiễu mỗi 10 điểm
        if i % noise_interval == 0:
            x1 = random.uniform(0, 10)
            x2 = random.uniform(0, 10)
        else:
            # Tạo dữ liệu theo phân phối chuẩn quanh trung tâm cụm
            x1 = np.random.normal(center[0], 1.4)
            x2 = np.random.normal(center[1], 1.4)

        # Giới hạn giá trị x1 và x2 trong khoảng 0-10
        x1 = max(0, min(20, x1))
        x2 = max(0, min(20, x2))

        # Thêm tuple vào dãy
        data.append((i, x1, x2))

    return data

# Sử dụng hàm để tạo dữ liệu với seed=42 để có thể tái tạo
num_points = 400
random_data = generate_data(num_points, seed=999)

# In ra một số dữ liệu để kiểm tra
for point in random_data[:10]:
    print(point)

# Lưu vào file CSV
import csv
csv_filename = "data1.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Index', 'X1', 'X2'])  # Write header
    csv_writer.writerows(random_data)

print(f"Data saved to {csv_filename}")

X = pd.read_csv('data1.csv')
X

import matplotlib.pyplot as plt

# Extract x1 and x2 from the tuples
x1_values = X.X1
x2_values = X.X2

# Plot the points
plt.figure(figsize = (15, 8))
plt.scatter(x1_values, x2_values, marker='o', label='Data Points')
plt.title('Biểu đồ phân tán giữa các điểm dữ liệu')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()

# Đọc data
values_X1 = X.X1
values_X2 = X.X2
# Lưu vào np.array
X = np.array([(x1, x2) for x1, x2 in zip(values_X1, values_X2)])

# Tạo mô hình
optics_model = OPTICS(eps=1.5, min_samples=50, cluster_method = 'dbscan')
optics_model.fit(X)

# Lấy ra giá trị reachability và nhãn
reachability_distances = optics_model.reachability_[optics_model.ordering_]
labels = optics_model.labels_

# Vẽ đồ thị
plt.figure(figsize=(15, 8))
plt.bar(range(len(reachability_distances)), reachability_distances, color='black')
plt.title('OPTICS Reachability Distances cho bộ 1')
plt.xlabel('Data Points')
plt.ylabel('Reachability Distance')

# Create a dictionary to map data points to their corresponding labels
data_labels = {f'Data Point {i}': label for i, label in enumerate(labels)}

# Visualize the assignment of each data point to its label
plt.figure(figsize=(15, 8))
# Define colors based on cluster labels
colors = {0: 'red', 1: 'blue', -1: 'green'}

# Scatter plot with custom colors
scatter = plt.scatter(X[:, 0], X[:, 1], c=[colors[label] for label in labels], edgecolor='k')
plt.title('Biểu đồ phân tán giữa các điểm dữ liệu của bộ 1.')
plt.xlabel('X1')
plt.ylabel('X2')

# Create a legend for the custom colors
legend_labels = ['Cluster 0', 'Cluster 1', 'Outlier']
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=10, label=f'Cluster {label}') for label in [0, 1, -1]]
plt.legend(handles=legend_elements, labels=legend_labels)

plt.show()

"""## Experiment 1: With different eps"""

eps_values = [0.5, 1.5, 2.5]

fig, axes = plt.subplots(1, len(eps_values), figsize=(18, 6), sharey=True)

for i, eps in enumerate(eps_values):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=eps, min_samples=50, cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Define colors based on cluster labels
    colors = {0: 'red', 1: 'blue', -1: 'green'}

    # Scatter plot with custom colors
    scatter = axes[i].scatter(X[:, 0], X[:, 1], c=[colors[label] for label in labels], edgecolor='k')
    axes[i].set_title(f'eps = {eps}')
    axes[i].set_xlabel('X1')
    axes[i].set_ylabel('X2')

    # Create a legend for the custom colors
    legend_labels = ['Cluster 0', 'Cluster 1', 'Outlier']
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=10, label=f'Cluster {label}') for label in [0, 1, -1]]
    axes[i].legend(handles=legend_elements, labels=legend_labels)

plt.show()

eps_values = [1.5, 2.5]

fig, axes = plt.subplots(1, 2, figsize=(18, 5), sharey=True)

for i, eps in enumerate(eps_values):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=eps, min_samples=50, cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Tính silhouette avg cho từng điểm dữ liệu
    silhouette_avg = silhouette_score(X, labels)
    print(f"Silhouette Score: {silhouette_avg}")
    # Tính silhouette score cho từng điểm dữ liệu
    silhouette_values = silhouette_samples(X, labels)

    # Vẽ silhouette plot
    y_lower = 10

    for j in range(len(np.unique(labels))):
        cluster_silhouette_values = silhouette_values[labels == j]
        cluster_silhouette_values.sort()

        size_cluster_j = cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_j

        color = plt.cm.viridis(float(j) / len(np.unique(labels)))

        axes[i].fill_betweenx(np.arange(y_lower, y_upper),
                              0, cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

        axes[i].text(-0.05, y_lower + 0.5 * size_cluster_j, str(j))

        y_lower = y_upper + 10

    axes[i].axvline(x=silhouette_avg, color="red", linestyle="--")
    axes[i].set_title(f'Silhouette plot for eps = {eps}')
    axes[i].set_xlabel("Silhouette Score")
    axes[i].set_ylabel("Cluster label")

plt.tight_layout()
plt.show()

"""## Experiment 2: With different MinPts"""

minpts_values = [40, 50, 60, 70]

fig, axes = plt.subplots(1, 4, figsize=(18, 6), sharey=True)

for i, minpts in enumerate(minpts_values):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=1.5, min_samples=minpts, cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Tính silhouette avg cho từng điểm dữ liệu
    silhouette_avg = silhouette_score(X, labels)
    print(f"Silhouette Score: {silhouette_avg}")
    # Tính silhouette score cho từng điểm dữ liệu
    silhouette_values = silhouette_samples(X, labels)

    # Vẽ silhouette plot
    y_lower = 10

    for j in range(len(np.unique(labels))):
        cluster_silhouette_values = silhouette_values[labels == j]
        cluster_silhouette_values.sort()

        size_cluster_j = cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_j

        color = plt.cm.viridis(float(j) / len(np.unique(labels)))

        axes[i].fill_betweenx(np.arange(y_lower, y_upper),
                              0, cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

        axes[i].text(-0.05, y_lower + 0.5 * size_cluster_j, str(j))

        y_lower = y_upper + 10

    axes[i].axvline(x=silhouette_avg, color="red", linestyle="--")
    axes[i].set_title(f'Silhouette plot for MinPts = {minpts}')
    axes[i].set_xlabel("Silhouette Score")
    axes[i].set_ylabel("Cluster label")

plt.tight_layout()
plt.show()

minpts_values = [5, 20, 50, 100]

fig, axes = plt.subplots(1, len(minpts_values), figsize=(18, 5), sharey=True)

for i, minpts in enumerate(minpts_values):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=1.5, min_samples=minpts, cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Bar plot for reachability distances with labels
    axes[i].bar(range(len(reachability_distances)), reachability_distances, color=plt.cm.viridis(labels / max(labels)), edgecolor='black')
    axes[i].set_title(f'Reachability plot for MinPoints = {minpts}')
    axes[i].set_xlabel("Data Points")
    axes[i].set_ylabel("Reachability distance")

plt.tight_layout()
plt.show()

"""## Experiment 3: With different distance measures"""

metrics = ['euclidean', 'manhattan']

fig, axes = plt.subplots(1, len(metrics), figsize=(18, 5), sharey=True)

for i, metric in enumerate(metrics):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=1.5, min_samples=50,
                          metric = metric,
                          cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Bar plot for reachability distances with labels
    axes[i].bar(range(len(reachability_distances)), reachability_distances, color=plt.cm.viridis(labels / max(labels)), edgecolor='black')
    axes[i].set_title(f'Reachability plot for metric = {metric}')
    axes[i].set_xlabel("Data Points")
    axes[i].set_ylabel("Reachability distance")

plt.tight_layout()
plt.show()

# Run OPTICS algorithm
optics_model = OPTICS(eps=1.5, min_samples=50,metric = 'cosine', cluster_method = 'dbscan')
optics_model.fit(X)

# Extract reachability distances and labels
reachability_distances = optics_model.reachability_[optics_model.ordering_]
labels = optics_model.labels_

# Plot the OPTICS result
plt.figure(figsize=(9,5))
# Bar plot for reachability distances
plt.bar(range(len(reachability_distances)), reachability_distances, color='black')
plt.title('Reachability plot for metric = cosine')
plt.xlabel('Data Points')
plt.ylabel('Reachability Distance')

"""# SET 2"""

# Dùng hàm để tạo biểu đồ hình bán nguyệt.
X, y = make_moons(n_samples=3000, noise=0.1, random_state=random_seed)

plt.figure(figsize=(15, 8))
plt.scatter(X[:, 0], X[:, 1], s=30, color='c')
plt.title('Biểu đồ phân tán hình mặt trăng.')
plt.xlabel("X1")
plt.ylabel("X2")

plt.show()
plt.clf()

# Lưu X vào CSV
np.savetxt('data2.csv', X, delimiter=',')

X = pd.read_csv('data2.csv', header=None)
X

# Run OPTICS algorithm
optics_model = OPTICS(eps = 0.15,min_samples=50, cluster_method = 'dbscan')
optics_model.fit(X)

# Extract reachability distances and labels
reachability_distances = optics_model.reachability_[optics_model.ordering_]
labels = optics_model.labels_

# Plot the OPTICS result
plt.figure(figsize=(15, 8))
# Bar plot for reachability distances
plt.bar(range(len(reachability_distances)), reachability_distances, color='black')
plt.title('OPTICS Reachability Distances cho bộ 2')
plt.xlabel('Data Points')
plt.ylabel('Reachability Distance')

# Create a dictionary to map data points to their corresponding labels
data_labels = {f'Data Point {i}': label for i, label in enumerate(labels)}

# Visualize the assignment of each data point to its label
plt.figure(figsize=(15, 8))
# Define colors based on cluster labels
colors = {0: 'red', 1: 'blue', -1: 'green'}

# Scatter plot with custom colors
scatter = plt.scatter(X[0], X[1], c=[colors[label] for label in labels], edgecolor='k')
plt.title('Biểu đồ phân tán giữa các điểm dữ liệu cho bộ 2.')
plt.xlabel('X1')
plt.ylabel('X2')

# Create a legend for the custom colors
legend_labels = ['Cluster 0', 'Cluster 1', 'Outlier']
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=10, label=f'Cluster {label}') for label in [0, 1, -1]]
plt.legend(handles=legend_elements, labels=legend_labels)

plt.show()

"""## Experiment 1: With different eps"""

eps_value = [0.05, 0.15, 0.165]

fig, axes = plt.subplots(1, len(eps_value), figsize=(18, 4), sharey=True)

for i, eps in enumerate(eps_value):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=eps, min_samples=50, cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Define colors based on cluster labels
    colors = {0: 'red', 1: 'blue', -1: 'green'}

    # Scatter plot with custom colors
    scatter = axes[i].scatter(X[0], X[1], c=[colors[label] for label in labels], edgecolor='k')
    axes[i].set_title(f'eps = {eps}')
    axes[i].set_xlabel('X1')
    axes[i].set_ylabel('X2')

    # Create a legend for the custom colors
    legend_labels = ['Cluster 0', 'Cluster 1', 'Outlier']
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=10, label=f'Cluster {label}') for label in [0, 1, -1]]
    axes[i].legend(handles=legend_elements, labels=legend_labels)

plt.show()

import matplotlib.cm as cm

fig, axes = plt.subplots(1, len(eps_value), figsize=(18, 4), sharey=True)

for i, eps in enumerate(eps_value):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=eps, min_samples=50, cluster_method='dbscan')
    optics_model.fit(X)

    # Extract labels
    labels = optics_model.labels_

    # Check if there are at least 2 clusters
    if len(np.unique(labels)) > 1:
        # Calculate silhouette scores
        silhouette_avg = silhouette_score(X, labels)
        print(f"Silhouette Score for eps = {eps}: {silhouette_avg}")
        silhouette_values = silhouette_samples(X, labels)

        y_lower = 10
        for j in range(len(np.unique(labels))):
            # Aggregate the silhouette scores for samples belonging to cluster j, and sort them
            ith_cluster_silhouette_values = silhouette_values[labels == j]
            ith_cluster_silhouette_values.sort()

            size_cluster_j = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_j

            color = 'skyblue' if j == 0 else 'pink'
            axes[i].fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            #axes[i].text(-0.05, y_lower + 0.5 * size_cluster_j, str(j))

            # Compute the new y_lower for the next plot
            y_lower = y_upper + 10

        # The vertical line for average silhouette score of all the values
        axes[i].axvline(x=silhouette_avg, color="red", linestyle="--")

        axes[i].set_title(f'Silhouette plot for eps = {eps}')
        axes[i].set_xlabel("Silhouette Score")
        axes[i].set_ylabel("Cluster label")
    else:
        fig.delaxes(axes[i])


plt.tight_layout()
plt.show()

"""## Experiment 2: With different MinPts"""

minpts_values = [30, 50, 70, 90]

fig, axes = plt.subplots(1, 4, figsize=(18, 6), sharey=True)

for i, minpts in enumerate(minpts_values):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=0.15, min_samples=minpts, cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Tính silhouette avg cho từng điểm dữ liệu
    silhouette_avg = silhouette_score(X, labels)
    print(f"Silhouette Score: {silhouette_avg}")
    # Tính silhouette score cho từng điểm dữ liệu
    silhouette_values = silhouette_samples(X, labels)

    # Vẽ silhouette plot
    y_lower = 10

    for j in range(len(np.unique(labels))):
        cluster_silhouette_values = silhouette_values[labels == j]
        cluster_silhouette_values.sort()

        size_cluster_j = cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_j

        color = plt.cm.viridis(float(j) / len(np.unique(labels)))

        axes[i].fill_betweenx(np.arange(y_lower, y_upper),
                              0, cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

        axes[i].text(-0.05, y_lower + 0.5 * size_cluster_j, str(j))

        y_lower = y_upper + 10

    axes[i].axvline(x=silhouette_avg, color="red", linestyle="--")
    axes[i].set_title(f'Silhouette plot for MinPts = {minpts}')
    axes[i].set_xlabel("Silhouette Score")
    axes[i].set_ylabel("Cluster label")

plt.tight_layout()
plt.show()

minpts_values = [5, 20, 50, 100]

fig, axes = plt.subplots(1, len(minpts_values), figsize=(18, 5), sharey=True)

for i, minpts in enumerate(minpts_values):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=0.15, min_samples=minpts, cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Bar plot for reachability distances with labels
    axes[i].bar(range(len(reachability_distances)), reachability_distances, color=plt.cm.viridis(labels / max(labels)), edgecolor='black')
    axes[i].set_title(f'Reachability plot for MinPoints = {minpts}')
    axes[i].set_xlabel("Data Points")
    axes[i].set_ylabel("Reachability distance")

plt.tight_layout()
plt.show()

"""## Experiment 3: With different distance measures"""

metrics = ['euclidean', 'manhattan']

fig, axes = plt.subplots(1, len(metrics), figsize=(18, 5), sharey=True)

for i, metric in enumerate(metrics):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=0.15, min_samples=50,
                          metric = metric,
                          cluster_method='dbscan')
    optics_model.fit(X)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Bar plot for reachability distances with labels
    axes[i].bar(range(len(reachability_distances)), reachability_distances, color=plt.cm.viridis(labels / max(labels)), edgecolor='black')
    axes[i].set_title(f'Reachability plot for metric = {metric}')
    axes[i].set_xlabel("Data Points")
    axes[i].set_ylabel("Reachability distance")

plt.tight_layout()
plt.show()

# Run OPTICS algorithm
optics_model = OPTICS(eps=0.15, min_samples=50,metric = 'cosine', cluster_method = 'dbscan')
optics_model.fit(X)

# Extract reachability distances and labels
reachability_distances = optics_model.reachability_[optics_model.ordering_]
labels = optics_model.labels_

# Plot the OPTICS result
plt.figure(figsize=(9,5))
# Bar plot for reachability distances
plt.bar(range(len(reachability_distances)), reachability_distances, color='black')
plt.title('Reachability plot for metric = cosine')
plt.xlabel('Data Points')
plt.ylabel('Reachability Distance')

"""# SET 3"""

import torch
from torchvision import datasets, transforms
from sklearn.cluster import OPTICS
import matplotlib.pyplot as plt

# Download bộ dữ liệu
transform = transforms.Compose([transforms.ToTensor(), transforms.Lambda(lambda x: x.view(-1))])
fashion_mnist_train = datasets.FashionMNIST(root='./data', train=True, transform=transform, download=True)

# Chọn ra lớp quan tâm và dát phẳng các hình trong mỗi lớp
selected_classes = [1, 4]
flattened_images = {i: [] for i in selected_classes}

for image, label in fashion_mnist_train:
    if label in selected_classes and len(flattened_images[label]) <= 99:
        flattened_images[label].append(image.numpy())
    else:
        continue

# Chuyển dạng từ mảng trong numpy sang tensor trong torch
for label in flattened_images:
    flattened_images[label] = torch.stack([torch.from_numpy(img) for img in flattened_images[label]])


for label in flattened_images:
    flattened_images[label] = flattened_images[label].view(flattened_images[label].size(0), -1)


all_flattened_images = torch.cat([flattened_images[label] for label in flattened_images], dim=0)

flattened_images[selected_classes[0]][0].size()

# Display 5 images from the first class along with their sizes
num_images_to_display = 5
first_class_label = selected_classes[0]

print(f"Class {first_class_label} - Shape: {flattened_images[first_class_label].shape}")
for i in range(num_images_to_display):
    plt.subplot(1, num_images_to_display, i + 1)
    image = flattened_images[first_class_label][i].numpy().reshape(28, 28)
    plt.imshow(image, cmap='gray')
    plt.axis('off')

plt.show()

# Display 5 images from the first class along with their sizes
num_images_to_display = 5
first_class_label = selected_classes[1]

print(f"Class {first_class_label} - Shape: {flattened_images[first_class_label].shape}")
for i in range(num_images_to_display):
    plt.subplot(1, num_images_to_display, i + 1)
    image = flattened_images[first_class_label][i].numpy().reshape(28, 28)
    plt.imshow(image, cmap='gray')
    plt.axis('off')

plt.show()

# Use OPTICS for clustering and create a reachability plot
optics_model = OPTICS(eps=0.11, min_samples=20,
                      metric = 'cosine',
                      cluster_method = 'dbscan')
optics_labels = optics_model.fit(all_flattened_images)

# Extract reachability distances and labels
reachability_distances = optics_model.reachability_[optics_model.ordering_]
labels = optics_model.labels_

# Plot the OPTICS result
plt.figure(figsize=(15, 8))
# Bar plot for reachability distances
plt.bar(range(len(reachability_distances)), reachability_distances, color='black')
plt.title('OPTICS Reachability Distances cho bộ 3')
plt.xlabel('Data Points')
plt.ylabel('Reachability Distance')

"""## Experiment 1: With different eps"""

eps_value = [0.11, 0.17, 0.2]

fig, axes = plt.subplots(1, len(eps_value), figsize=(18, 4), sharey=True)

for i, eps in enumerate(eps_value):
    optics_model = OPTICS(eps=eps, min_samples=20, metric='cosine', cluster_method = 'dbscan')
    optics_model.fit(all_flattened_images)

    labels = optics_model.labels_

    if len(np.unique(labels)) > 1:
        silhouette_avg = silhouette_score(all_flattened_images, labels)
        print(f"Điểm silhouette cho eps = {eps}: {silhouette_avg}")
        silhouette_values = silhouette_samples(all_flattened_images, labels)

        y_lower = 10
        for j in range(len(np.unique(labels))):
            ith_cluster_silhouette_values = silhouette_values[labels == j]
            ith_cluster_silhouette_values.sort()

            size_cluster_j = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_j

            color = cm.nipy_spectral(float(j) / len(np.unique(labels)))
            axes[i].fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7)

            y_lower = y_upper + 10

        axes[i].axvline(x=silhouette_avg, color="red", linestyle="--")

        axes[i].set_title(f'Silhouette plot for eps = {eps}')
        axes[i].set_xlabel("Silhouette score")
        axes[i].set_ylabel("Cluster label")
    else:
        fig.delaxes(axes[i])

plt.tight_layout()
plt.show()

"""## Experiment 2: With different MinPts"""

minpts_values = [10, 20, 30, 40]

fig, axes = plt.subplots(1, len(minpts_values), figsize=(18, 4), sharey=True)

for i, minpts in enumerate(minpts_values):
    optics_model = OPTICS(eps=0.11, min_samples=minpts, metric='cosine', cluster_method = 'dbscan')
    optics_model.fit(all_flattened_images)

    labels = optics_model.labels_

    if len(np.unique(labels)) > 1:
        silhouette_avg = silhouette_score(all_flattened_images, labels)
        print(f"Điểm silhouette khi MinPts = {minpts}: {silhouette_avg}")
        silhouette_values = silhouette_samples(all_flattened_images, labels)

        y_lower = 10
        for j in range(len(np.unique(labels))):
            ith_cluster_silhouette_values = silhouette_values[labels == j]
            ith_cluster_silhouette_values.sort()

            size_cluster_j = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_j

            color = cm.nipy_spectral(float(j) / len(np.unique(labels)))
            axes[i].fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color, alpha=0.7)

            y_lower = y_upper + 10

        axes[i].axvline(x=silhouette_avg, color="red", linestyle="--")

        axes[i].set_title(f'Silhouette plot for MinPts = {minpts}')
        axes[i].set_xlabel("Silhouette score")
        axes[i].set_ylabel("Cluster label")
    else:
        continue

plt.tight_layout()
plt.show()

minpts_values = [10, 20, 30, 40]

fig, axes = plt.subplots(1, len(minpts_values), figsize=(18, 4), sharey=True)


for i, minpts in enumerate(minpts_values):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=0.11, min_samples=minpts, metric = 'cosine', cluster_method='dbscan')
    optics_model.fit(all_flattened_images)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Bar plot for reachability distances with labels
    axes[i].bar(range(len(reachability_distances)), reachability_distances, color=plt.cm.viridis(labels / max(labels)), edgecolor='black')
    axes[i].set_title(f'Reachability plot for MinPoints = {minpts}')
    axes[i].set_xlabel("Data Points")
    axes[i].set_ylabel("Reachability distance")

plt.tight_layout()
plt.show()

"""## Experiment 3: With different distance measures"""

metrics = ['euclidean', 'manhattan']

fig, axes = plt.subplots(1, len(metrics), figsize=(18, 5), sharey=True)

for i, metric in enumerate(metrics):
    # Run OPTICS algorithm
    optics_model = OPTICS(eps=0.11, min_samples=20,
                          metric = metric,
                          cluster_method='dbscan')
    optics_model.fit(all_flattened_images)

    # Extract reachability distances and labels
    reachability_distances = optics_model.reachability_[optics_model.ordering_]
    labels = optics_model.labels_

    # Bar plot for reachability distances with labels
    axes[i].bar(range(len(reachability_distances)), reachability_distances, color='black')
    axes[i].set_title(f'Reachability plot for metric = {metric}')
    axes[i].set_xlabel("Data Points")
    axes[i].set_ylabel("Reachability distance")

plt.tight_layout()
plt.show()

# Run OPTICS algorithm
optics_model = OPTICS(eps=0.15, min_samples=50,metric = 'cosine', cluster_method = 'dbscan')
optics_model.fit(all_flattened_images)

# Extract reachability distances and labels
reachability_distances = optics_model.reachability_[optics_model.ordering_]
labels = optics_model.labels_

# Plot the OPTICS result
plt.figure(figsize=(9,5))
# Bar plot for reachability distances
plt.bar(range(len(reachability_distances)), reachability_distances, color='black')
plt.title('Reachability plot for metric = cosine')
plt.xlabel('Data Points')
plt.ylabel('Reachability Distance')






