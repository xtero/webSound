from flask import Flask
from flask_restful import Resource, Api
import os
import vlc
from random import randint

base_dir = os.path.dirname(os.path.realpath(__file__))

def get_random_file( directory ):
        file_list = os.listdir( directory )
        file_id = randint( 0, len( file_list ) - 1 )
        file_name = file_list[ file_id ]
        return directory+"/"+file_name

class Good(Resource):
    def get(self):
        file_name = get_random_file( base_dir + "/sounds/good" )
        p = vlc.MediaPlayer('file://'+ file_name )
        p.play()
        return file_name

class Bad(Resource):
    def get(self):
        file_name = get_random_file( base_dir + "/sounds/bad" )
        p = vlc.MediaPlayer('file://'+ file_name )
        p.play()
        return file_name

app = Flask(__name__)
api = Api(app)

api.add_resource( Good, '/good' )
api.add_resource( Bad, '/bad' )

if __name__ == '__main__':
     app.run(port=5002)
