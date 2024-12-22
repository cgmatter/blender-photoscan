import numpy as np
import plyfile

# Read the PLY file
data = plyfile.PlyData.read(r"C:\Users\barro\Desktop\model_dense.ply")

# Create a new list of vertices without the unwanted properties
vertices = []
for vertex in data['vertex']:
    filtered_vertex = (
        vertex['x'],
        vertex['y'],
        vertex['z'],
        vertex['red'],
        vertex['green'],
        vertex['blue'],
    )
    vertices.append(filtered_vertex)

# Define the new PLY structure without the unwanted attributes
vertex_dtype = [
    ('x', 'f4'),
    ('y', 'f4'),
    ('z', 'f4'),
    ('red', 'u1'),
    ('green', 'u1'),
    ('blue', 'u1'),
]
filtered_vertex_data = np.array(vertices, dtype=vertex_dtype)

# Create the new PLY structure
filtered_ply = plyfile.PlyData([
    plyfile.PlyElement.describe(filtered_vertex_data, 'vertex')
], text=True)

# Write the filtered PLY file
filtered_ply.write(r"C:\Users\barro\Desktop\model_dense_out.ply")
