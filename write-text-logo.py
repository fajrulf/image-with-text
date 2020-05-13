from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_title(text,name):
    #wrap text with maximum of 15 character per line
    wrap = textwrap.wrap(text, width=15)
    #number of line of the text
    n = len(wrap)

    #define the canvas size
    max_w, max_h = 1200, 675
    #create the canvas with certain size and color
    im = Image.new('RGB', (max_w, max_h), (65, 214, 239))
    #define drawing variable of the canvas
    draw = ImageDraw.Draw(im)
    #define font with certain type and size
    font = ImageFont.truetype(
       '/HelveticaNeueLTStd-Blk.otf', 80)

    #spacing between line
    space = 30
    #width and heigh of text
    w, h = draw.textsize(wrap[0])
    #define initial height to center the text + logo vertically
    current_h = ((MAX_H - (n*h + (n-1)*space) ) / 2) - 1.5*h

    #write text line by line
    for line in wrap:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font)
        current_h += h + space

    #open and read logo file
    logo = Image.open('logo.png', 'r')
    logo_w, logo_h = logo.size
    offset = (((max_w - logo_w)/2) , (current_h + h))
    offset = (int(offset[0]),int(offset[1]))
    
    #add logo to images
    im.paste(logo, offset)
    #save images
    im.save('output/'+name)
