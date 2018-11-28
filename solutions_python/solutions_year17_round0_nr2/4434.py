
# coding: utf-8

# In[1]:

num_ = 99998


# In[11]:

def is_tidy_(num_):
    digits_ = str(num_)
    position_ = 0
    while position_ < (len(digits_) - 1):
        if digits_[position_] > digits_[position_+1]:
            return False
        position_ += 1
    return True


# In[98]:

def find_last_tidy_num_(num_):
    if is_tidy_(num_):
        return num_
    
    num_str_ = str(num_)
    num_digits_ = len(num_str_)
    if len(num_str_) >= 3:
        base_span_ = 1
        while True:
            if base_span_ > num_digits_:
                base_span_ -= 1
                break
            if is_tidy_(int(num_str_[0:base_span_])):
                base_span_ += 1
                continue
            else:
                base_span_ -= 1
                break
        while True:
            part_1_ = str(int(num_str_[0:base_span_]) - 1)
            if is_tidy_(part_1_):
                break
            base_span_ -= 1
            if base_span_ < 1:
                raise BaseException("Error for >= 3")
        part_2_ = "".join(["9" for counter_ in range(num_digits_-base_span_)])
        return int(part_1_ + part_2_)
    elif len(num_str_) == 2:
        if num_ < 20:
            return 9
        else:
            part_1_ = str(int(num_str_[0]) - 1)
            part_2_ = "9"
            return int(part_1_ + part_2_)
    else:
        raise BaseException("Error for == 1")


# In[113]:

lines_in_ = []
with open("B-small-attempt0.in", "r") as file_in_:
    for val_ in file_in_.readlines():
        lines_in_.append(int(val_))

if lines_in_:
    data_in_ = [int(lines_in_[line_num_]) for line_num_ in range(1, lines_in_[0] + 1)]

with open("B-small-attempt0.in.out", "w") as file_out_:
    for index_, num_ in enumerate(data_in_):
        file_out_.write("Case #")
        file_out_.write(str(index_ + 1))
        file_out_.write(": ")
        file_out_.write(str(find_last_tidy_num_(num_)))
        if index_ < len(lines_in_) - 2:
            file_out_.write("\n")


# In[ ]:



