import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# generating a random unit_vector maintaining spherically uniformness is not trivial
# it can be done using a gaussian distribution generally, or spherical coordinates in 3d
# here we will use another approach: generating random vectors by coordinates in a cube, and discarding those
# outside a sphere cointained inside the cube


def random_unit_vector_sph_unif():
    while True:
        candidate = np.random.uniform([-2, -2, -2], [2, 2, 2])
        candidate_sq_norm = np.dot(candidate, candidate)
        if candidate_sq_norm < 4:
            break

    unit_vector = candidate / np.linalg.norm(candidate)

    return unit_vector


def orth_proyection(unit_vector, vector):
    proyection = unit_vector * np.dot(unit_vector, vector)

    return proyection


def random_orth_unit_vector(unit_vector):
    rand_u_vec = random_unit_vector_sph_unif()
    proyection = orth_proyection(unit_vector, rand_u_vec)  # be carefull with order
    random_orth_vector = rand_u_vec - proyection

    return random_orth_vector / np.linalg.norm(random_orth_vector)


def perpendicular_unit_vector(unit_vector1, unit_vector2):
    return np.cross(unit_vector1, unit_vector2)


def cube():
    vertix = np.empty([8, 3])

    vertix[0] = [0, 0, 0]
    vertix[1] = random_unit_vector_sph_unif()
    vertix[2] = random_orth_unit_vector(vertix[1])
    vertix[3] = vertix[1] + vertix[2]

    perpendicular_aux = perpendicular_unit_vector(vertix[1], vertix[2])

    for i in range(4, 8):
        vertix[i] = vertix[i - 4] + perpendicular_aux

    return vertix

def plot_cube():
    # Define the eight vertices of the cube
    vertices = cube()

    # Define the six faces of the cube using the vertices
    faces = [
        [vertices[0], vertices[1], vertices[3], vertices[2]],
        [vertices[4], vertices[5], vertices[7], vertices[6]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],

    ]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the cube
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    # Show the plot
    plt.show()

    # for i in range(0,7):  #validation, all dot products must be either 0,1 or 2.
    #     for j in range(0,7):
    #         print(np.dot(vertices[i],vertices[j]))

def main():
    return


if __name__ == '__main__':
    main()
