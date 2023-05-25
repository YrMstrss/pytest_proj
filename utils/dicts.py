def get_val(collection, key, default='git'):
    keys = []
    for k in collection.keys():
        keys.append(k)

    if key in keys:
        return collection[key]
    else:
        return default
