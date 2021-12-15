from PIL import Image, ImageDraw, ImageFont
import boto3
from pprint import pprint, pformat
from io import BytesIO
from image_helpers import get_image


# AWS rekognition
def label_image(img, confidence=50):
   

    client = boto3.client('rekognition')
    imagebytes = get_image(img)
    response = client.detect_labels(Image={"Bytes": imagebytes}, MaxLabels= 10, MinConfidence=70)
    pprint(response)
    pillow_image = get_pillow_img(imagebytes)

    (img_w, img_h) = pillow_image.size
    x1 = img_w/2-100
    y1 = img_h - 100
    x2 = img_w/2-100
    y2 = img_h/2-80

    # label = ''
    for object in response['Labels']:
        print ("Label: " + object['Name'])
        label = object['Name']
        if label == "Hot Dog":
            print("Hot Dog")
            image = add_text_to_img(pillow_image, "Hot Dog", pos=(x2,y2), color=(255,255,255), bgcolor=(0,200,0))
            return image

    # if label != "Hot Dog":
    print("Not Hot Dog")
    image1 = add_text_to_img(pillow_image, "Not Hot Dog", pos=(x1,y1), color=(255,255,255), bgcolor=(200,0,0))
    return image1


if __name__ == "__main__":
    # can't use input since PyCharm's console causes problems entering URLs
    # img = input('Enter either a URL or filename for an image: ')
    # img = 'https://render.fineartamerica.com/images/rendered/default/poster/8/10/break/images/artworkimages/medium/1/pizza-slice-diane-diederich.jpg'
    img = 'https://i.kinja-img.com/gawker-media/image/upload/s--6RyJpgBM--/c_scale,f_auto,fl_progressive,q_80,w_800/tmlwln8revg44xz4f0tj.jpg'
    # img = 'https://media-cdn.tripadvisor.com/media/photo-s/17/3b/9a/d2/burger-king.jpg'
    labelled_image = label_image(img)
    labelled_image.show()
