import cv2
import pandas as panda

img_path = r'E:\B.TECH\btech 8th semester study material\final year project\color-pic-image.jpg'
img = cv2.imread(img_path)



clicked = False

#setting initially cursor at origin(left-top-most) 
r=0
g=0
b=0
x_pos=0
y_pos=0


#naming field names on the basis of records from csv value
index=["color","color-name","hex","R","G","B"]
csv=panda.read_csv('colors.csv',names=index,header=None)



# function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):
    min=1000
    for i in range(len(csv)):
        d=abs(R-int(csv.loc[i,"R"])) + abs(G-int(csv.loc[i,"G"])) + abs(B-int(csv.loc[i,"B"]))
        if d <= min:
            min = d
            cname = csv.loc[i,"color_name"]
    return cname



#function to get x,y cordinates of mouse double click
def drawFunction(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,x_pos,y_pos,clicked
        clicked = True
        x_pos = x
        y_pos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image',drawFunction)

while True:
    cv2.imshow("image",img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()