import yaml
import xml.etree.ElementTree as xml_tree
from xml.dom import minidom

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', { 
     'version':'2.0',
     'xmlns:podcast':'https://podcastindex.org/namespace/1.0',
     'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
     'xmlns:content':'http://purl.org/rss/1.0/modules/content/',
     'xmlns:atom':'http://www.w3.org/2005/Atom',
     'xml:lang':'en'})
    
channel_element = xml_tree.SubElement(rss_element, 'channel')

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'link').text = yaml_data['link']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'itunes:image', {'href': yaml_data['image']})
xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']})

for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'link').text = item['file']
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']
    xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']
    xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
    
    xml_tree.SubElement(item_element, 'enclosure', {
        'url': item['file'],
        'type': 'audio/mpeg',
        'length': str(item['length'])
    })

# Edit the xml file to be more readable
xml_str = minidom.parseString(xml_tree.tostring(rss_element)).toprettyxml(indent='  ')
xml_str = '\n'.join([line for line in xml_str.split('\n') if line.strip()])
xml_str = xml_str.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="UTF-8"?>', 1)

with open('podcast.xml', 'w') as f:
    f.write(xml_str)
