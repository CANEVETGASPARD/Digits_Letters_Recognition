import matplotlib.pyplot as plt
import numpy as np
import copy

#trying to display picture
#in our case we have only 28*28 picture

def display_pictures(data,height_picture,width_picture, height_plot, width_plot,debug=False):
    data_without_label = data.iloc[:,1:] #remove label columns (index 0)
    picture_list = []
    picture_matrix = np.array(np.zeros([height_picture,width_picture]))

    for picture in range(data_without_label.shape[0]):

        if(debug):
            print("picture_id :",picture)
        # init row and col index to fill in picture matrix with the proper pixel
        # -> picture are shaped in 1-D list in our data set and we have to shaped them in 28*28 matrix
        row = 0
        col = 0
        for pixel in range(data_without_label.shape[1]):

            if(debug):
                print("row :",row)
                print("col :",col)
                print("pixel :",pixel)

            if(col==width_picture): #reinit at the end of the row
                col = 0
                row += 1

            picture_matrix[col,row] = data_without_label.iloc[picture,pixel]
            col += 1


        picture_list.append(copy.deepcopy(picture_matrix))

    plot_picture(picture_list, width_plot, height_plot)

    pass


def plot_picture(list_of_picture,plot_width,plot_height):
    N=len(list_of_picture)

    if (N==1):
        plt.figure(figsize=(1/2,1/2))
        plt.title(f'plot {N} sample of the data')
        plt.imshow(list_of_picture[0],cmap="gray_r")
        plt.axis("off")

    else:
        fig, ax = plt.subplots(plot_height, plot_width,figsize=(plot_width, plot_height))
        fig.suptitle(f'plot {N} sample of the data')

        if(plot_width==1 or plot_height==1): #prevent error in the case of 1-D subplots
            for picture_id in range(N):
                ax[picture_id].imshow(list_of_picture[picture_id],cmap="gray_r")
                ax[picture_id].axis("off")

        else :
            row = 0
            col = 0
            for picture_id in range(N):
                if(col==plot_width):
                    col=0
                    row += 1
                ax[row,col].imshow(list_of_picture[picture_id],cmap="gray_r")
                ax[row,col].axis("off")
                col += 1
        plt.tight_layout()
        plt.show()

    pass


#plot data set distribution
def plot_data_distribution(data,label_columns):
    plt.title("distrubution of the current data set")
    data_set_groupbylabel = data.groupby(by=label_columns).count().iloc[:,0]
    data_set_groupbylabel.plot.bar()
    plt.xlabel("data label")
    plt.ylabel("count")

    pass