
#replace selected markers from page source to readable characters
def replaceMathToReadableCharacters(text):
    text = text.replace(r'\\n', u'\n')
    text = text.replace(r'\\xa0', u' ')
    text = text.replace(r'\\\\/', u'/')
    text = text.replace(r'\\\\', u'')
    text = text.replace(r'lor', u'v')
    text = text.replace(r'sqrt{', u'√(')
    text = text.replace(r'frac{', u'(')
    text = text.replace(r'}{', u')/(')
    text = text.replace(r'}', u')')
    text = text.replace(r'&ge', u'>=')
    text = text.replace(r'geq', u'>=')
    text = text.replace(r'&gt', u'>')
    text = text.replace(r'&lt', u'<')
    text = text.replace(r'&le', u'<=')
    text = text.replace(r'^{', u'^(')
    text = text.replace(r'log_{', u'log_(')
    text = text.replace(r',', u', ')
    text = text.replace(r'in {', u'∈ <')
    return text