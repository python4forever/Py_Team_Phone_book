def get_data(path, sep):
    db_dicts = []
    keys = ['id', 'surname', 'name', 'patronymic', 'phone', 'comment']
    with open(path, 'r', encoding='utf-8') as db:
        for i in db:
            db_dicts.append(dict(zip(keys, i.split(sep))))
    return db_dicts
