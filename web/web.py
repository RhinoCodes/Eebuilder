import webbrowser

files = []
class NewPage:
    def __init__(self, name, lang="", css="", title=""):
        

        self.name = name
        self.file = name+'.html'
        if title=="":
            title = self.file
        open(self.file, 'w+').close()
        with open(self.file, "w+") as f:
            f.write(f"""
            <!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>{title}</title>
    <link href="{css}" rel="stylesheet" type="text/css" />
  </head>
  <body>
            """)


    def pic(self, path):
        f = open(self.file, 'a+')
        f.write("<img src='%s'>" %path)
        f.close()


    def title(self, text):
        f=open(self.file+'.html', 'a+')
        if file=='all':
            for item in files:
                f=open(self.file, 'a+')
                f.write('<title>%s</title>'% text)
                f.close()
        else:
            f = open(self.file+'.html', 'a')
            f.write('<title>%s</title>'% text)
            f.close()

    def header(self, text, centered=False):
            f=open(self.file, 'a+')
            if centered==True:
                f.write('<h1 style="text-align: center;">'+text+'</h1>')
            elif centered==False:
                f.write('<h1>'+text+'</h1>')
            f.close()

    def text(self, text, centered=False):
            f=open(self.file, 'a+')
            if centered==False:
                f.write('<p>'+text+'</p>')
            elif centered==True:
                f.write('<p  style="text-align: center;">'+text+'</p>')
            f.close()

    def link(self, page, text, style='text', centered=False):
        f=open(self.file, 'a+')
        if style=='text':
            if centered==True:
                f.write('<a href='+page+'.html>'+text+'</h1>')
            else:
                f.write('<a href='+page+'.html>'+text+'</h1>')
        elif style=='button':
            if centered==True:
                f.write("""
            <form>
            <input style='text-align: center;' type="button" value="""+text+""" onclick="window.location.href='"""+page+"""'" />
            </form>
                    """)
            else:
                f.write("""
        <form>
        <input type="button" value="""+text+""" onclick="window.location.href='"""+page+"""'" />
        </form>
                """)
            f.close()

    def search(self, centered=False):
        f=open(self.file, 'a+')
        if centered==True:
            f.write("""
            <div id='a' style='text-align:center;'>
            <input type='text' id='link_id'>
            <input type='button' id='link' value='Search' onClick='javascript:goTo()'>
            </div>
            <script>
            function goTo()
            {
                input = document.getElementById('link_id').value;
                location.href = 'https://www.google.com/search?safe=active&source=hp&ei=qBgiXYDCFtDVtAay2ovIAg&q='+input+'&oq='+input+'p&gs_l=psy-ab.3..0l10.4800.5462..5922...0.0..1.236.818.5j2j1......0....1..gws-wiz.....0..0i131j0i3.wh3C02wdyCM&safe=active'
            }
            </script>
                """)
        else:
            f.write("""
        <input type='text' id='link_id'>
        <input type='button' id='link' value='Search' onClick='javascript:goTo()'>
        <script>
        function goTo()
        {
            input = document.getElementById('link_id').value;
            location.href = 'https://www.google.com/search?safe=active&source=hp&ei=qBgiXYDCFtDVtAay2ovIAg&q='+input+'&oq='+input+'p&gs_l=psy-ab.3..0l10.4800.5462..5922...0.0..1.236.818.5j2j1......0....1..gws-wiz.....0..0i131j0i3.wh3C02wdyCM&safe=active'
        }
        </script>
            """)
        f.close()

    def piclink(self, page, path):
        f = open(self.file+'.html', 'a+')
        f.write("""
        <a href='"""+self.name+""".html'>
        <img src='"""+path+"""'>
        </a>
            """)
        f.close()

    def start(self):
        webbrowser.open_new(self.file)
