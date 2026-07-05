import os
import copy
compilers="javac --release 8 "
decompilers="openjdk-asmtools-jdis $1.class -w . "
print("\033c\033[47;31m\ngive me file to jbat: ? \n")
#a="Hello.java"
a=input().strip()
b=a.replace(".java","")
os.system(compilers + a)
os.system(decompilers.replace("$1",b)  )
os.rename("$1.jasm".replace("$1",b),"$1.jbat".replace("$1",b))