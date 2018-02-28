# -*- coding: utf-8 -*-
# @Project : my_web
# @Time    : 0228
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : app.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from tornado import web, ioloop, httpserver


class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


application = web.Application([
    (r"/", MainPageHandler),
])


def main():
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
