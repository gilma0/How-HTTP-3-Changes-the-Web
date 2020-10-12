import shutil

# this is a tool we created for easier creation of synthetic websites for testing

# html builder with the amount of the objects to be loaded
def copy_text(times):
    outF = open("index.html", "w")
    outF.write("""<h1 style="color: #5e9ca0;" data-darkreader-inline-color="">object overload demo</h1>""")
    outF.write("\n")
    for i in range(1, times):
        outF.write("""<P><A HREF="/misc/igloo_nav.map"><IMG ISMAP USEMAP="#mainmap" SRC=""" + '"' + str(i) + """.gif" BORDER=0 HEIGHT=400 WIDTH=800></A><BR>
<!--TOOLBAR_END--><!--HEADER_START--></P>""")
        outF.write("\n")
    outF.close()

# file duplicate creator with different names to be loaded (different name is a must so that each file will be requested by the web browser)
def copy_paste(name, times): 
    for i in range(1, times):
        target = "duplicated object destination path" + str(i) + ".gif"
        shutil.copy(name, target)



if __name__ == '__main__':
    #copy_paste('path of object to be duplicated', 50)
    copy_text(50)

