import flask, flask_migrate, flask_sqlalchemy
import os

project = flask.Flask(
    import_name="main",
    instance_path= os.path.abspath(__file__ + "../"),
    template_folder="templates"
)

#project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
#
#db = flask_sqlalchemy.SQLAlchemy(app = project)
#
#migrate = flask_migrate.Migrate(app = project, db = db)