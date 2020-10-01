from tika import parser 
import os

def read_pdf(filename):
    raw = parser.from_file(filename)
    return raw

def write_to_file(filename,raw):
    f = open(filename,"x",encoding="utf-8")
    f.write(raw['content'])
    f.close()

def main():
    file_to_read = input("File to read : ")
    file_to_write = input("File to write : ")
    cont = read_pdf(file_to_read)
    write_to_file(file_to_write,cont)

main()
                
