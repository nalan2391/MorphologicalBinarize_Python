import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage.filters import try_all_threshold
from skimage.filters import threshold_mean
from skimage.filters import threshold_minimum
from skimage.filters import threshold_otsu, threshold_local
import matplotlib.image as mpimg
from skimage import color
from skimage import io
from skimage import data


def mor_bin():
 
    # Load the image.
    imge = io.imread('images/T2-Tumor.png',as_grey=True)
    
    height,width = imge.shape
    
    img_th = threshold_otsu(imge) 

    th_low = img_th*0.8 #lower thresold 
    th_high = img_th*1.3 #higher threshold
    

    for i in range(width):
    	for j in range(height):

    		if( i==0 or j==0 or i==width-1 or j==height-1):

    			imge[j,i] = 1
    			
    		else:

	    		if(imge[j,i]>th_high):

	    			imge[j,i]=1

	    		elif(imge[j,i]<th_low):

	    			imge[j,i]=0


    for i in range (1,width-1):
    	for j in range(1,height-1):

    		if(imge[j,i] != 0 and imge[j,i] != 1):

    			if ( imge[j,i+1]==0 and imge[j,i-1]==0 and imge[j+1,i]==0 and imge[j-1,i]==0 ):
    				imge[j,i] = 0 #as foreground
    			
    			else:
    				imge[j,i] = 1 #else background
    			

	    		if (imge[j,i+1]==1 or imge[j,i-1]==1 or imge[j+1,i]== 1 or imge[j-1,i]==1 ):

    				imge[j,i] = 1 #as background 
    				


   # plt.axis("off")
    plt.imshow(imge,cmap=plt.cm.gray)
    plt.show()
   # 



if __name__ == '__main__':
 
#work with grayscale images 
#98% accuracy compared to Mathematica's MorphologicalBinarize Function 

    mor_bin()
