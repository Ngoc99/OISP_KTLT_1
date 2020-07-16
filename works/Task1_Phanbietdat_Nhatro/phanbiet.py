import utils
import re

def phanbiet(dict_input: dict) -> int:
    
    """Phân biệt các post Nhà trọ hoặc dãy nhà trọ hoặc dãy trọ (realestate_type = 7).
    BĐS có mục đích bán.
    """
    realestate_type = dict_input['realestate_type']
    content = dict_input['content']

    if (realestate_type == 7):
        new_content = remove_accents(content)
       
        # Post chứa các keyword:
        # dãy trọ, nhà trọ, dãy nhà trọ, dãy phòng trọ

        regex_daytro = "day (nha |phong )?tro|nha tro"
        result_daytro= re.search(regex_daytro, new_content)

        # Nếu không có keyword thì không thuộc type 7, trả về -1
        if (result_daytro is None):
            realestate_type = -1
        else:
            realestate_type = 7

    return realestate_type
