
def log(i_data, i_debug = False, o_log_file = None, i_force = False):
    """
    i_data : The data to be written
    i_debug (bool) : True if the data should be printed
    o_log_file (file) : An opened file, or None if there is
    no file to be written to
    """

    if i_force or i_debug:
        print(i_data)
    if o_log_file:
        o_log_file.write(str(i_data) + '\n')

