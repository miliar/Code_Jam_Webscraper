def output_to(file_name, text, type='w'):
    f = open(file_name, type)
    f.write(text)
    f.close()