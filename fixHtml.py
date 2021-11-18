import ftfy
import codecs

fileName = ["Diesel.html","Marni.html","Margiela.html","Staff.html"]


for name in fileName:

    f = codecs.open(name, "r","utf-8")
    #print(ftfy.fix_text(f.read(18745)))


    text_file = codecs.open("fix" + name, "w", "utf-8")
    text_file.write(ftfy.fix_text(f.read()))
    text_file.close()
