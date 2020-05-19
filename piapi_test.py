#! /usr/bin/env python3


class PIAPITest(object):

    def __init__(self):        
        # Store all the response codes in faster lookups
        # NOTE: response and response_json MUST have the same name in _parse()
        self.status_codes = {
            302: ('Incorrect credentials provided{0}', "''", ),
            400: ('Invalid request: {0}', "response_json['errorDocument']['message']", ),
            401: ('Unauthorized access{0}', "''", ),
            403: ('Forbidden access to the REST API{0}', "''", ),
            404: ('URL not found: {0}', "str('http://example.com')", ),
            406: ('The Accept header sent in the request does not match a supported type{0}', "''", ),
            415: ('The Content-Type header sent in the request does not match a supported type{0}', "''", ),
            500: ('An error has occured during the API invocation{0}', "''", ),
            502: ('The server is down or being upgraded{0}', "''", ),
            503: ('The servers are up, but overloaded with requests. Try again later (rate limiting){0}', "''", ),
        }
        self.test_cases = (200, 302, 400, 401, 403, 404, 406, 415, 500, 502, 503, 666, )

    def _parse(self):
        response_json = {
            'errorDocument': {
                'message': 'Some cool error message',
            },
        }

        for response_code in self.test_cases:
            error_message = self.status_codes.get(response_code)
            if response_code == 200:
                print({'yes': 'good content here', })
            elif error_message:
                print("Raising error", error_message[0].format(eval(error_message[1])))
            else:
                print("Raising error: Unknown Request Error, return code is {0}".format(response_code))

if __name__ == '__main__':
    t = PIAPITest()
    t._parse()
