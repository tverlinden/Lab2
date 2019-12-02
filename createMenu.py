def createMenu(optionList):
    tmp = ''
    for (n, option) in enumerate(optionList, 1):
        tmp += '{}. {}\n'.format(n, option)
    return tmp
