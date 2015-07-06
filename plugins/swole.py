import os, sys
import pickle
import threading
import json
import random   

# change where to look for imports
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(here, '..')))
print os.getcwd()

from User import User

CONFIG_FILE = '../slackbot-workout/config.json'
CACHE_FILE = '../slackbot-workout/user_cache.save'

CONFIG = json.load(open(CONFIG_FILE))


def callouts(bot):
  se.main(bot)

def process_message(data):
  print data
  if data['channel'].startswith("D"):
    text = data['text'].encode('ascii', 'ignore')
    user_id = data['user']
    user_cache = pickle.load(open(CACHE_FILE, 'rb'))
    user = user_cache[user_id]
    print user.username
    if ('swole' in text.lower()) or ('stat' in text.lower()):
      motivator = getMotivationalContent()
      print motivator
      outputs.append([data['channel'], motivator])
      s = getUserExercise(user)
      print s
      outputs.append([data['channel'], s])
    # send out stats
    elif ('done' in text):
      #complete and send stat
      outputs.append([data['channel'],"YOU GO GLEN COCO"])
  if data['channel'].encode('ascii','ignore') == 'C06T76C8N':
      text = data['text'].encode('ascii', 'ignore')
      if ('done' in text.lower()):
        motivator = getMotivationalContent()
        outputs.append([data['channel'], motivator])

def getUserExercise(user):
  exercises = CONFIG["exercises"]
  s = "```\n"
  for (ex_id,reps) in user.exercises.iteritems():
    exercise_name = exercises[ex_id]['name'].encode('ascii','ignore') 
    exercise_units = exercises[ex_id]['units'].encode('ascii', 'ignore')
    #TODO: pluralize using inflect package
    s += exercise_name + ": " + str(reps) + " " + exercise_units+'s' + "\n"
  s += "```\n"
  return s

def getMotivationalContent():
  fname = "motivate.txt"
  lines = open(fname).read().splitlines()
  return random.choice(lines)
#rtm = threading.Thread(target=process_message, args=(data))
#calloutThread = threading.Thread(target=callouts, args=(bot))

#rtm.start()
#calloutThread.start()

