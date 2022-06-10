from tkinter import *
from tkinter import ttk


# Global Variables
postCount = 0;


def new_post(tree, posts, postTitle, postQuality):
    """Checks user input boxes for values that will be used as parameters for the forum post, then posts it to the window."""

    # Variables
    global postCount # TODO: Does this really need to be global?
    postValues = [] # List of forum post values

    # Put a list of new post values into the list of all posts
    # [iid, upvotes, title, quality]
    postValues.extend((postCount, int(0), postTitle.get(), postQuality.get()))
    posts.append(postValues)

    # Put post title and quality into their respective fields on the Treeview
    tree.insert(parent='', index='end', iid=postCount, text='', values=(postValues[1], postValues[2], postValues[3]))
    postCount += 1
    

def iterate(tree):
    print(tree.item(0, "values"))


def run_simulation():
    print("TODO")


def update_sim_speed():
    print("TODO")


def batch_sim():
    print("TODO")


def build_treeview(frame):

    # Variables
    columnWidth = 52

    # Main stuff
    tree = ttk.Treeview(frame)

    # Define columns
    tree['columns'] = ("votes", "title", "quality")

    # Format columns
    # Treeview requires you to have a phantom first column called "#0".
    # If the tree doesn't have hierarchical items (i.e. click "+" to expand), the width of this column can be set to 0.
    tree.column("#0", width=0, stretch=NO, anchor=W)
    tree.column("votes", width=columnWidth+3, stretch=NO, anchor=CENTER) # I need to do +3 to the width, otherwise it's misaligned by 1 pixel for some reason grr
    tree.column("title", width=columnWidth*2-1, stretch=NO, anchor=W)
    tree.column("quality", width=columnWidth-1, stretch=NO, anchor=CENTER)

    # Headings
    tree.heading("#0", text="", anchor=W)
    tree.heading("votes", text="votes", anchor=CENTER)
    tree.heading("title", text="title", anchor=W)
    tree.heading("quality", text="quality", anchor=CENTER)

    # Return treeview
    return tree



def build_main_window():

    # Variables
    buttonWidth=16
    posts = [] # List of all the forum posts and their values

    # Main stuff
    root = Tk()
    root.title = "Karma Simulation"
    frame = ttk.Frame(root, padding=1)
    frame.grid()

    # Treeview window
    # Give it root and frame, and get from it some fields that we can put on the grid below
    tree = build_treeview(frame)

    # Entry widgets
    postTitle = StringVar()
    postTitleEntry = ttk.Entry(frame, textvariable = postTitle, width=buttonWidth)
    postQuality = StringVar()
    postQualityEntry = ttk.Entry(frame, textvariable = postQuality, width=int(buttonWidth/2))
    simSpeed = StringVar()
    simSpeedEntry = ttk.Entry(frame, textvariable = simSpeed, width=int(buttonWidth/2)-1)

    # Define width of columns
    frame.columnconfigure(0,weight=2)
    frame.columnconfigure(1,weight=2)
    frame.columnconfigure(2,weight=1)
    frame.columnconfigure(3,weight=2)
    frame.columnconfigure(4,weight=2)
    frame.columnconfigure(5,weight=2)
    frame.columnconfigure(6,weight=2)

    # Place widgets into the grid
    ttk.Label(frame, text="", width=7).                                                                             grid(column=0, row=0)
    ttk.Label(frame, text="", width=1).                                                                             grid(column=1, row=0)
    postTitleEntry.                                                                                                 grid(column=2, row=0)
    postQualityEntry.                                                                                               grid(column=3, row=0)
    ttk.Button(frame, text="New Post", command=lambda: new_post(tree, posts, postTitle, postQuality), width=buttonWidth).  grid(column=4, row=0, columnspan=2, sticky=W)
    ttk.Button(frame, text="Iterate", command=lambda: iterate(tree), width=buttonWidth).                            grid(column=4, row=1, columnspan=2, sticky=W)
    tree.                                                                                                           grid(column=0, row=1, columnspan=4, rowspan=600, sticky=W) #treeview seems to insert width into each rows unless I make rowspan sufficiently high
    ttk.Button(frame, text="Run", command=run_simulation, width=buttonWidth).                                       grid(column=4, row=2, columnspan=2, sticky=W)
    ttk.Button(frame, text="Speed:", command=update_sim_speed, width=int(buttonWidth/2)).                           grid(column=4, row=3, columnspan=1, sticky=W)
    simSpeedEntry.                                                                                                  grid(column=5, row=3, columnspan=1, sticky=W)
    ttk.Button(frame, text="Batch Sim", command=batch_sim, width=buttonWidth).                                      grid(column=4, row=6, columnspan=2, sticky=W)

    # Mainloop
    root.mainloop()
