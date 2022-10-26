class Config:
	SECRET_KEY = 'B!1weNAt1T^%KVHuI*S^'

class DevelopmentConfig(Config):
	DEBUG=True 
	MYSQL_HOST = 'localhost'
	MYSQL_USER = 'root'
	MYSQL_PASSWORD = 'cuaderno23'
	MYSQL_DB = 'usuarios'


config={
	'development':DevelopmentConfig
}


