SERVER_ICON = u'\uf0ae'

def add_hostname_nucleus_segment(powerline):
    from socket import gethostname
    if powerline.args.colorize_hostname:
        from lib.color_compliment import stringToHashToColorAndOpposite
        from lib.colortrans import rgb2short
        hostname = gethostname().upper()
        if hostname.startswith("DEV-DUTCH-"):
            host_prompt = ' %s %s' % (SERVER_ICON, hostname[10:12])
        else:
            host_prompt = ' %s %s' % (SERVER_ICON, hostname.split('.')[0])
        FG, BG = stringToHashToColorAndOpposite(hostname)
        FG, BG = (rgb2short(*color) for color in [FG, BG])

        powerline.append(host_prompt, FG, BG)
    else:
        hostname = gethostname().upper()

        if hostname.startswith("DEV-DUTCH-"):
            host_prompt = ' %s %s' % (SERVER_ICON, hostname[10:12].upper())
            BG = Color.HOSTNAME_BG
        else:
            host_prompt = ' %s %s' % (SERVER_ICON, hostname.split('.')[0])
            BG = Color.USERNAME_ROOT_BG

        powerline.append(host_prompt, Color.HOSTNAME_FG, BG)