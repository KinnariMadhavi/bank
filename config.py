class Config(object):

	#common Configuration
	SECRET_KEY= ''
	# SQLALCHEMY_DATABASE_URI = '<use_database>://<username>:<password>@<IP>/<database_name>'
	SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/bank_db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

	#Development configurations

	DEBUG = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):

	#Production configurations
	DEBUG = False


app_config = {
	'development':DevelopmentConfig,
	'production': ProductionConfig
}