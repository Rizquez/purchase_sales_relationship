from config import config
from routes.routes import app

if __name__ == '__main__':
    app.config.from_object(config['development_debug'])
    app.run()
    