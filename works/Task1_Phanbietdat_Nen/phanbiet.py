import re

def remove_accents(input_str):
    """
    * Đổi các ký tự từ Uicode sang dạng không dấu và in thường

    * Arguments:
        input_str {str} -- string cần chuyển đổi

    * Returns:
        str -- string nếu chuyển đổi thành công
        None - otherwise
    """

    S1 = "ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ"
    S0 = "AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy"

    if input_str is None:
        return 'none'

    s = ""
    for c in input_str:
        if c in S1:
            s += S0[S1.index(c)]
        else:
            s += c
    return s.lower()


def phanbiet(dict_input: dict) -> int:
    """
    * Phân biệt đất nền (10).

    * Arguments:
        inp_str {dict} -- dict chứa 3 thông tin sau:
            id              : id của bài đăng
            content         : content của bài đăng
            realestate_type : loại bất động sản
    * Returns:
        int - realestate_type mới của bài đăng
    """

    realestate_type = dict_input['realestate_type']

    if (realestate_type == 1):
        dict_content = remove_accents(dict_input['content'])

        pattern1 = "dat\s+(nen|nen\s+tho\s+cu|du\s+an|xay\s+dung)|khu\s+du\s+an|nen\s+dat|phan\s+lo|dat_nen"
        result1 = re.search(pattern1, dict_content)

        """
        * Test xem có chứa từ khoá của đất thổ cư và nông nghiệp không

        pattern2 = "len\s+tho\s+cu|len\s+100%\s+tho\s+cu|dat\s+tho\s+cu|dat\s+tc|dat\s+o\s+tai\s+(do\s+thi|nong\s+thon)|dat\s+trong\s+cay|dat\s+nong\s+nghiep|dat\s+lam\s+nghiep"
        result2 = re.search(pattern2, dict_content)
        if (result1 is not None):
            print("{0} {1}".format(dict_input['id'], result2 is not None))
		"""

        if (result1 is not None):
            realestate_type = 10

############################
# Return
############################
    return realestate_type
