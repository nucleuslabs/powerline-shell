USER_ICON = u'\uf183'

def add_username_nucleus_segment(powerline):
    import os
    user_prompt = '%s%s' % (USER_ICON, os.getenv('USER')[:2].upper())

    if os.getenv('USER') == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
    else:
        bgcolor = Color.USERNAME_BG

    powerline.append(user_prompt, Color.USERNAME_FG, bgcolor)
