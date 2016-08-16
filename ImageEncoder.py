import base64
from urllib2 import Request, urlopen

class FacialRecognition:
    app_id = ''
    app_key = ''

    def encode_image_base64(self, path_name):
        with open(path_name, 'rb') as image_file:
            data = image_file.read()
            base64_image = data.encode('base64')
            return base64_image

    #initialize
    def __init__(self, path_name=None):
        self.app_id = 'c97ffb85'
        self.app_key = '2af79610a214e023c27cda68f49286ea'

        if path_name is not None:
            base64_image = self.encode_image_base64(path_name)
            self.enroll_image(base64_image)
        
    def enroll_image(self, base64_image):
        print('Enrolling Image')
        values = "{ \"image\": \"" + str(base64_image) + "\", \"subject_id\": \"dummy\", \"gallery_name\": \"testgallery1\" }"

        headers = {
            'Content-Type': 'application/json',
            'app_id': str(self.app_id),
            'app_key': str(self.app_key)
            }
        
        request = Request('https://api.kairos.com/enroll', data=values, headers=headers)
        response_body = urlopen(request).read()
        print 'Printing Response...'
        print response_body

    def recognize_image(self, path_name):
        base64_image = self.encode_image_base64(path_name)
        
        print('Recognizing Image')
        values = "{ \"image\": \"" + str(base64_image) + "\", \"gallery_name\": \"testgallery1\" }"

        headers = {
            'Content-Type': 'application/json',
            'app_id': str(self.app_id),
            'app_key': str(self.app_key)
            }
        
        request = Request('https://api.kairos.com/recognize', data=values, headers=headers)
        response_body = urlopen(request).read()
        print 'Printing Response...'
        print response_body
