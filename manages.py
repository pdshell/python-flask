from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from models import User

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本命令manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
