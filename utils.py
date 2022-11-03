def build_query(cmd, val, file_list):
    if cmd == 'filter':
        #res = [x for x in file_list if val in x]
        res = filter(lambda x: val in x, file_list)
        return res
    if cmd == 'map':
        val = int(val)
        res = [x.split(' ')[val] for x in file_list]
        return res
    if cmd == 'unique':
        res = list(set(file_list))
        return res
    if cmd == 'sort':
        reverse = val == 'desc'
        res = sorted(file_list, reverse=reverse)
        return res
    if cmd == 'limit':
        val = int(val)
        res = list(file_list)[:val]
        return res


