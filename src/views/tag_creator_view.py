from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        #body = http_request.body
        #product_code = body["product_code"]

        #logica de regra de negócio
        print('Estou na minha view')
        print(http_request)
        #retorno http
        return HttpResponse(status_code=200, body={"Hello": "world"})