#extract text from pdf and read it using google text to speech

import PyPDF2, os
from gtts import gTTS
from sys import argv


pdf_name = argv[1]
txt_name = str(pdf_name.split("/")[-1].split(".")[-2]) + ".txt"
mp3_name = str(pdf_name.split("/")[-1].split(".")[-2]) + ".mp3"


def text_extractor():
    with open(f'{pdf_name}','rb') as pdf_file, open(f'{txt_name}', 'w',encoding='utf-8') as text_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        all_pages = pdf_reader.getNumPages()
        for page_number in range(all_pages):   
            page = pdf_reader.getPage(page_number)
            content = page.extractText()
            text_file.write(content)


def text_to_speech():
    file_to_read = open(f'{txt_name}', 'r')
    text = file_to_read.read()
    language = 'en'
    output = gTTS(text = text, lang=language, slow=False)
    output.save(f'{mp3_name}')
    file_to_read.close()


text_extractor()
text_to_speech()
