# Machine-Learning
OPTICS
# Topic objectives 
  + The goal of this project is to focus on discovering, understanding, and applying the OPTICS algorithm in the field of Machine Learning and data analysis. We set specific goals as follows:
      - Deeper understanding of OPTICS: Conduct detailed research on the operating mechanism, calculation principles, and process for determining the group structure based on the density of the OPTICS algorithm.
      - Apply to real problems: Apply OPTICS to real problems in Machine Learning.
      - Evaluate advantages and limitations: Further analysis of the advantages and limitations of OPTICS. This includes processing different types of data that other algorithms cannot handle.
      - Identify effective use cases: Capture specific cases where OPTICS can be effectively applied, and provide recommendations on its use in real-world complex situations.
  + Our ultimate goal is to provide an extensive and comprehensive overview of OPTICS, from theory to practice, helping readers better understand the potential and limitations of this algorithm in processing and data analysis.
# Data description
  + 1st data set
    ![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/4306bd5e-4541-47c6-8306-2ba230f10a8f)
  + 2nd dataset
    ![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/19661b36-ba6a-4a26-ba55-993d733a62b7)
  + 3rd dataset
    ![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/55d58f0e-8500-4d65-82cf-e61a2c3ab139)
# Introducing the OPTICS algorithm
  + OPTICS (Ordering Points To Identify the Clustering Structure) is a clustering algorithm proposed in 1999. OPTICS is considered an extension algorithm of DBSCAN.
  + The OPTICS algorithm will arrange data points based on the reachability distance of those points, and based on that reachability distance, we can draw a chart showing the reachability distance. plot). Consecutive points in the graph whose distance approaches less than a threshold value are considered to belong to the same cluster.
  + To go deeper into the algorithm, we need to understand the basic concepts in density-based clustering (Ester et al., 1996):
    - Directly density-reachable: A data point p is considered directly accessible based on density from data point q with two parameters ε and MinPts if:
        p is a point located in the neighborhood of point q (radius ε) and the number of data points in the neighborhood of point q must be greater than or equal to MinPts (this condition is also known as the core object condition). condition)).
        Illustration as shown in the figure (Sharma, n.d.) (Y in this case is q, X in this case is p):
![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/714b8f80-d77f-4e73-aff9-68efcb8917e6)

    - Density-reachable: A data point p is considered reachable based on density from data point q with two parameters ε and MinPts if there exists a sequence of data points from p1 to pn ( p1 in this case is q, pn in this case is p) where pi+1 can be approached directly from pi with two parameters ε and MinPts
    - Density-connected: 2 data points p and q are considered densely connected if there exists a data point o such that both points p and q can be accessed based on density from both points p and q. Illustration as shown in the figure (Ankerst et al., 1999):
![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/b185184d-0813-4509-992d-9efd7a733b97)

    - Cluster: The authors of the report define a cluster as a non-empty set that meets two conditions:
        Maximality: For all data points p and q belonging to the set of points D: If point p belongs to cluster C and q can be accessed based on the density from p, then q is also a point from cluster C.
        Connectivity: For all data points p and q belonging to cluster C: p is densely connected to q.
    - Noise: Points that do not belong to any cluster are considered noise.
  + After mentioning the concepts of density-based clustering, we come to other concepts when the author develops the OPTICS algorithm in addition to the existing concepts as mentioned above:
    - Core-point/core-object: A point that has at least MinPoints (MinPts) other points in its vicinity, with radius ε. This means that a core point is a point located in the center of a dense set of points. However, the core point is not necessarily the center point of the cluster. For example, in a data set with two overlapping clusters, there may be a core point located between the two clusters. In this case, the core point is not the center of any cluster.
    - Core-distance: The core distance of a data point p is the smallest distance to the MinPtsth point in the neighborhood ε of that point p (under the condition that point p meets the core condition mentioned above). above).
    - Reachability-distance: Is the distance from a point to the nearest core point in its vicinity. In case that point is a core point, the reachability distance will be equal to the core - distance. Reachability distance indicates which cluster a point is likely to belong to based on the distance to surrounding core points. If the reachability - distance of a point is small, then that point has a high probability of belonging to the cluster of the nearest core point. On the contrary, if the reachability - distance of a point is large, then that point may belong to another cluster or may be an outlier.
    - Results of the OPTICS (Clustering order) clustering algorithm: As discussed above, the OPTICS algorithm is not a normal clustering algorithm. For example, we have a data set containing n points. The OPTICS algorithm, after running on this data set, will generate an order of new points (also n points) and these new points are also stored along with their approach distance (this approach distance ≥ 0). We can draw a column chart based on the sorted data set and produce the following figure:
![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/a46e8a3e-bf12-4659-823a-892c16f51197)

→ So we have gone through the author's definitions of the OPTICS algorithm, next we observe specifically how the algorithm will be carried out.
# Model results
+ 1st data set
    ![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/242d970d-625a-440e-a052-ee74fef1c9fe)
  + 2nd dataset
    ![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/4649f939-8b9a-4efb-abc0-4668f5c3b364)
  + 3rd dataset
    ![image](https://github.com/MQuynh/Machine-Learning/assets/120617972/2dcf83cd-8499-4553-85c0-9aaf22adbf0b)
