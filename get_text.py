import requests, urllib
import spacy
import en_core_web_sm

# -------------------------------------
# IN COMMAND LINE DO THIS
# python -m spacy download en_core_web_sm
# -------------------------------------

#
# EXISTING FNC
#

def send_a_pdf_to_api_and_get_text_from_api(file_url):
    local_file = 'local_copy.pdf'
    # it's the internal api 
    # is used to send pdf-file and get document_id
    post_url = "http://localhost:5000/documents"
    urllib.request.urlretrieve(file_url, local_file)

    files = {"file": open(local_file, "rb")}

    # send file
    response = requests.post(post_url, files=files)
    
    # api is configured to return documenet_id
    # get id of the document saved in database
    document_id = response.json()['id']

    # getting data from api
    get_url = "http://localhost:5000/text/"+str(document_id)+".txt"

    # the api is configured to return text when document_id is sent
    response = requests.get(get_url)
    # print(response.text['text'])
    text_from_file = response.json()

    return text_from_file['text']


#
#
#
def get_text_without_references(text):
    '''
    Extracts only text, and skips refenreces
    '''
    try:
        reference_word = 'Introduction'
        # the first character to cut hte text out
        first_word = text.find(reference_word)
    except Exception:
        pass

    try:
        reference_word = 'Reference'
        text_without_references = text[first_word:text.find(reference_word)]
    except Exception:
        pass
    return text_without_references


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


#
#
#
def save_named_entities_to_array(text):
    '''
    Extract named entities from text without references
    '''
    # list_of_named_entities = ''
    list_of_named_entities = []
    # list_of_named_entities = {}

    nlp = en_core_web_sm.load()
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON" and len(ent.text) > 7 and not has_numbers(ent.text):
            # list_of_named_entities = list_of_named_entities + ' - ' + ent.text
            list_of_named_entities.append(ent.text)
    
    list_of_named_entities = list(dict.fromkeys(list_of_named_entities))
    return list_of_named_entities




text = send_a_pdf_to_api_and_get_text_from_api('https://arxiv.org/pdf/cs/9308101v1.pdf')
text_wo_ref = get_text_without_references(text)
# print(text_wo_ref)

array_of_named_entities = save_named_entities_to_array(text)
print(array_of_named_entities)

# 
# simple text
#
'''
text = 'Billy wants money from David'
array_of_named_entities = save_named_entities_to_array(text)
print(array_of_named_entities)
'''