w, h = 1000, 150

# frame per seconds
fps = 30
# duration of the movie
seconds = 4
# calculate the lenght of a single frame
duration = 1 / fps
# calculate the amount of frames needed
totalFrames = seconds * fps

def map(num, in_min, in_max, out_min, out_max):
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

for i in range(totalFrames):
    newPage(w, h)
    fill(0.93333333333,0.87450980392,0.82352941176)
    rect(0, 0, 1000, 150)

    frameDuration(duration)
    fill(0.80392156862,0.16078431372,0.14901960784)
    fontSize(100)
    p = "/Users/nouf.aljowaysir/Desktop/Taub Display/Taub Display Variable/TaubDisplay-C.ttf"
    font(p)
    value = map(i,0,totalFrames,0,1000)
    #if i < totalFrames/2:
        #value = map(i,0,totalFrames/2,0,90)
    #else:
        #value = map(i,totalFrames/2,totalFrames,90,0)
    fontVariations(wght=value)
    text("Taub Type is responsive", (15, 40))
    #saveImage('~/Desktop/animation#3/' + str(i) + ".png")

saveImage('~/Desktop/sentence-TaubDisplayA.gif')
for axis, data in listFontVariations().items():
    print((axis, data))
print("Done")
