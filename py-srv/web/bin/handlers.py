from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient

class SmokeTestHandler(RequestHandler):
    def get(self):
        self.write({"hello": "world"})

class GetHandler(RequestHandler):
    async def get(self):
        http = AsyncHTTPClient()
        results = await http.fetch("http://py-api-srv:8000/pop")
        self.write(results.body)
 
#    async def delete(self, pop_id):
#        http = AsyncHTTPClient()
#        results = await http.fetch(f"http://py-api-srv:8000/pop/{pop_id}")
#        self.write(results)
#
#class GetByFilterHandler(RequestHandler):
#    async def get(self, pop_id):
#        http = AsyncHTTPClient()
#        results = await http.fetch(f"http://py-api-srv:8000/pop/{pop_id}")
#        self.write(results)
#
#class InsertHandler(RequestHandler):
#    async def put(self, pop_name, pop_color):
#        http = AsyncHTTPClient()
#        results = await http.fetch(f"http://py-api-srv:8000/pop/{pop_name}/{pop_color}")
#        self.write(results)
#
#class UpdateHandler(RequestHandler):
#    async def post(self, pop_id, pop_name, pop_color):
#        http = AsyncHTTPClient()
#        results = await http.fetch(f"http://py-api-srv:8000/pop/{pop_id}/{pop_name}/{pop_color}")
#        self.write(results)
#