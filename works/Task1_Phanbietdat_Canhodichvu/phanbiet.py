
import re
import json
from utils import remove_accents

def phanbiet(dict_input: dict) -> int:
    """Phân biệt căn hộ dịch vụ .

    Arguments:
        inp_str {dict} -- dict chứa 3 thông tin sau:
            id              : id của bài đăng
            content         : content của bài đăng
            realestate_type : loại bất động sản
    Returns:
        int - realestate_type mới của bài đăng
    """

    realestate_type = dict_input['realestate_type']

    ## code goes here
    content = dict_input['content']
    if (realestate_type == 3):
        # remove Vietnameses accent from content using built-in function
        new_content = remove_accents(content)

        # find all the post that has such keyword by using regex rules
        regex_rule = "can\s+ho\s+dich\s+vu|chdv"
        
        result = re.search(regex_rule, new_content)

        if (result is not None):
            realestate_type = 2
        else:
            realestate_type = 3

    ############################
    ## Return
    ############################
    return realestate_type

