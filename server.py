import web

urls = (
    "/","hello",
)

app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello world'

class Redirect:
    def GET(self, path):
        web.seeother('/' + path + "/")

if __name__ == "__main__":
    app.run()
