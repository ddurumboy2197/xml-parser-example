import xml.etree.ElementTree as ET

def oqish(xml_fayl):
    tree = ET.parse(xml_fayl)
    root = tree.getroot()
    itemlar = root.findall('.//item')
    return itemlar

xml_fayl = 'xml_fayl.xml'  # XML fayliningizni yuklab oling
itemlar = oqish(xml_fayl)
for item in itemlar:
    print(item.text)
```

```python
import xml.etree.ElementTree as ET

class XmlOqish:
    def __init__(self, xml_fayl):
        self.tree = ET.parse(xml_fayl)
        self.root = self.tree.getroot()

    def oqish(self):
        return self.root.findall('.//item')

xml_fayl = 'xml_fayl.xml'  # XML fayliningizni yuklab oling
oqish = XmlOqish(xml_fayl)
itemlar = oqish.oqish()
for item in itemlar:
    print(item.text)
