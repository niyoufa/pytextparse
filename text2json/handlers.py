import handler

class HTMLRenderer(handler.Handler):
    """
    HTML 处理程序,给文本块加相应的 HTML 标记
    """
    def start_document(self):
        print('<html><head><title>ShiYanLou</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p style="color: #444;">')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2 style="color: #68BE5D;">')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul style="color: #363736;">')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1 style="color: #1ABC9C;">')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return('<em>%s</em>' % match.group(1))

    def sub_url(self, match):
        return('<a target="_blank" style="text-decoration: none;color: #BC1A4B;" href="%s">%s</a>' % (match.group(1), match.group(1)))

    def sub_mail(self, match):
        return ('<a style="text-decoration: none;color: #BC1A4B;" href="mailto:%s">%s</a>' % (match.group(1), match.group(1)))

    def feed(self, data):
        print(data)