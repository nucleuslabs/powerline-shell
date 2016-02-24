SERVER_ICON = u'\uf0ae'
# This is a nucleus specific development version with pretty icons and a much shoortened dev hostname
def add_hostname_nucleus_segment(powerline):
    import os
    if powerline.args.colorize_hostname:
        from lib.color_compliment import stringToHashToColorAndOpposite
        from lib.colortrans import rgb2short
        # this is not the recommended way to get hostname but it is faster and this is a very specific case
        hostname = os.getenv('HOST').upper()
        if hostname.startswith("DEV-DUTCH-"):
            host_prompt = ' %s %s' % (SERVER_ICON, hostname[10:12])
        else:
            host_prompt = ' %s %s' % (SERVER_ICON, '%m')
        FG, BG = stringToHashToColorAndOpposite(hostname)
        FG, BG = (rgb2short(*color) for color in [FG, BG])

        powerline.append(host_prompt, FG, BG)
    else:
        # this is not the recommended way to get hostname but it is faster and this is a very specific case
        hostname = os.getenv('HOST').upper()
        if hostname.startswith("DEV-DUTCH-"):
            host_prompt = ' %s %s' % (SERVER_ICON, hostname[10:12])
            BG = Color.HOSTNAME_BG
        else:
            host_prompt = ' %s %s' % (SERVER_ICON, '%m')
            BG = Color.USERNAME_ROOT_BG

        powerline.append(host_prompt, Color.HOSTNAME_FG, BG)