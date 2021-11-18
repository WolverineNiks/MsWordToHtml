import ftfy
import codecs

fileName = ["Marni.html"]
filesPath = "C:\\Users\\nikhi\\Documents\\GitHub\\MsWordToHtml\\HtmlFiles\\"
for name in fileName:

    f = codecs.open(filesPath+name, "r","utf-8")
    #print(ftfy.fix_text(f.read(18745)))


    text_file = codecs.open("fix" + name, "w", "utf-8")
    text_file.write(ftfy.fix_text(f.read()))
    text_file.close()
