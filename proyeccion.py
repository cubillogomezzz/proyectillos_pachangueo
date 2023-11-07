import definir_cubo as decu
import numpy as np
import matplotlib.pyplot as plt

def plane_orth_proj(plane_norm_unit_vec,vector):
        plane_proj = vector - decu.orth_proyection(plane_norm_unit_vec,vector)

        return plane_proj

def cube_plane_orth_proj(plane_norm_unit_vec,cube):
        points = np.empty([8,3])
        for i in range(0,7):
                points[i] = plane_orth_proj(plane_norm_unit_vec,cube[i])

        return points

def plot_proj_cubo(proy_cubo):
        # Sample points
        points = proy_cubo
        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the points
        ax.scatter(*zip(*points), c='r', marker='o')

        # Set axis limits
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])

        # Set axis labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Show the plot
        plt.show()

def main():
        print("hello")
        u = decu.cube()
        n = np.array([0,0,1])
        u_XY = cube_plane_orth_proj(n,u)
        print(u_XY)
        plot_proj_cubo(u_XY)
        decu.plot_cube(u)




if __name__ == '__main__':
        main()