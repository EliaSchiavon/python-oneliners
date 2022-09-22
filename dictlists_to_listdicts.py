from itertools import product


def dictlists_to_listdicts(dict_of_lists: dict) -> list:
    
    """
    Convert a dict with lists to a list of dicts
    """

    field_names = list(dict_of_lists.keys())
    values_lst = list(product(*dict_of_lists.values()))

    return [dict(zip(field_names, values)) for values in values_lst]


dict_of_lists = {'Field1': ['A', 'B', 'C'],
                 'Field2': [1, 2]}


list_of_dicts = dictlists_to_listdicts(dict_of_lists)


# simple unit test
expected_out_length = len(list(product(*dict_of_lists.values())))
assert len(list_of_dicts ) == expected_out_length
for subdict in list_of_dicts:
    assert subdict.keys() == dict_of_lists.keys()
    for k in subdict:
        # the value in each subdict in the list should not be more a list
        assert not isinstance(subdict[k], list) 
        assert subdict[k] in dict_of_lists[k]