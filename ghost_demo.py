from ghost import Ghost
import sys

def demo( url ):
	ghost = Ghost()
	session = ghost.start()
	session.open( url )
	print session.content


if __name__ == '__main__' :
	reload( sys )
	sys.setdefaultencoding('utf-8')

	demo( sys.argv[1].strip() )
