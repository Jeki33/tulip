import turtle as tu   
import re   
import docx

# Load the Word document
data = docx.Document("Tulipanes.docx")
coordinates = []   
colour = []

# Regular expressions for coordinates and colors
patron = r'[-+]?\d*\.\d*(?:[eE][-+]?\d+)?'
patron_coord = r'\(' + patron + r' ?\, ?' + patron
patron_color = patron_coord + r' ?\, ?' + patron + r'\)'

# Process paragraphs in the document
for i in data.paragraphs:   
    try:
        coord_stg_tup = re.findall(patron_coord + r'\)', i.text)
        color_stg_tup = re.findall(patron_color, i.text)

        if color_stg_tup:
            color_val = re.findall(r'[-+]?\d*\.\d*', color_stg_tup[0])   
            color_val_lst = [float(k) for k in color_val]   
            colour.append(tuple(color_val_lst))

        coord_num_tup = []      
        for j in coord_stg_tup:   
            coord_pos = re.findall(r'[-+]?\d*\.\d*', j)   
            coord_num_lst = [float(k) for k in coord_pos]   
            coord_num_tup.append(tuple(coord_num_lst))   

        coordinates.append(coord_num_tup)   
    except Exception as e:   
        print(f"Error processing paragraph: {e}")   
 
# Set up turtle graphics
pen = tu.Turtle()   
screen = tu.Screen()   

tu.tracer(2)   
tu.hideturtle()   
pen.speed(10)
screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)

# Draw shapes based on coordinates and colors
for i in range(len(coordinates)):   
    draw = 1   
    path = coordinates[i]   
    col = colour[i]   
    pen.color(col)   
    pen.begin_fill()   
    for order_pair in path:   
        x, y = order_pair   
        y = -1 * y   
        if draw:   
            pen.up()   
            pen.goto(x, y)   
            pen.down()   
            draw = 0   
        else:   
            pen.goto(x, y)   
    pen.end_fill()   
    pen.hideturtle()  

# Keep the window open
screen.mainloop()
