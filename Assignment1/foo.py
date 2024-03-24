import random
import math

class Cluster:
    def __init__(self):
        self.center = None
        self.points = []

def distance(point1, point2):
    return abs(point1 - point2)

def kmeans(data, k):
    # 创建空的聚类列表
    clusters = [Cluster() for _ in range(k)]

    # 在给定的数据点上选择初始聚类中心
    initial_centers = [data[0], data[2] ,data[5]]
    for i, center in enumerate(initial_centers):
        clusters[i].center = center

    # 迭代过程
    # prev_clusters = None
    # while clusters != prev_clusters:
    for i in range(3):
    
        prev_clusters = list(clusters)

        # 清空聚类中的数据点
        for cluster in clusters:
            cluster.points = []

        # 将每个数据点分配给最近的聚类中心
        for point in data:
            closest_cluster = min(clusters, key=lambda cluster: distance(cluster.center, point))
            closest_cluster.points.append(point)

        # 更新聚类中心
        for cluster in clusters:
            if cluster.points:
                cluster.center = sum(cluster.points) / len(cluster.points)
            # e#lse:
                # 若聚类中没有数据点，则随机选择一个数据点作为新的聚类中心
                # cluster.center = random.choice(data)

    return clusters

# 示例数据点
data = [16, 19, 20, 36, 39, 53]
# 聚类数量
k = 3

# 运行 k-means 算法并生成聚类
clusters = kmeans(data, k)

# 打印聚类
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: Center={cluster.center}, Points={cluster.points}")