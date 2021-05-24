def obj_to_str(object):
    if not object:
        return False
    string = codecs.encode(pickle.dumps(object), "base64").decode()
    return string


def str_to_obj(string: str):
    object = pickle.loads(codecs.decode(string.encode(), "base64"))
    return object
