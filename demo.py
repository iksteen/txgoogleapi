from twisted.internet import defer
from twisted.internet.task import react
import txgoogleapi
import urllib


requester = txgoogleapi.OAuthRequester(
    client_id='197556848193.apps.googleusercontent.com',
    client_secret='C8SEr93mw2pYUWeoM550bRcx',
    refresh_token='1/W77G51zBoTGSp6v9qzIvQjGlT65SCO0vHQO_Jpap7Rc',
    access_token='ya29.GltABN6cXBj2E_Y2YG5TBcTnI54M9dHkJJMU4O-heE1xjT2kFzYt0gO3rMJ59WBp02ILdmE3EUJwwe2c9jN8zStVUAT63eihfKZpdLI19QObJwjQ8q_yxOhS5hGX',
)
google = txgoogleapi.Google(requester)


@defer.inlineCallbacks
def main(reactor):
    result = yield google.youtube.search(
        part='snippet',
        q='jemoeder',
        maxResults=1,
        order='relevance',
        type='video',
    )
    item = result['items'][0]
    print 'https://www.youtube.com/watch?' + urllib.urlencode({'v': item['id']['videoId']})

react(main)
