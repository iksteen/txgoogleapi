from txgoogleapi.base import GoogleApi, GoogleApiEndPoint, SET, BOOL, INT, DATETIME


class Playlists(GoogleApiEndPoint):
    _url = '/playlists'
    _methods = {
        'list': {
            'method': 'GET',
            'required': {
                'part': SET('id', 'snippet', 'status'),
            },
            'filter': {
                'channelId': str,
                'id': str,
                'mine': BOOL,
            },
            'optional': {
                'maxResults': INT,
                'onBehalfOfContentOwner': str,
                'onBehalfOfContentOwnerChannel': str,
                'pageToken': str
            },
        },
        'insert': {
            'method': 'POST',
            'required': {
                'part': SET('snippet', 'status'),
            },
            'optional': {
                'onBehalfOfContentOwner': str,
                'onBehalfOfContentOwnerChannel': str,
            },
        },
        'update': {
            'method': 'PUT',
            'required': {
                'part': SET('snippet', 'status'),
            },
            'optional': {
                'onBehalfOfContentOwner': str,
            },
        },
        'delete': {
            'method': 'DELETE',
            'required': {
                'id': str,
            },
            'optional': {
                'onBehalfOfContentOwner': str,
            },
        },
    }


class PlaylistItems(GoogleApiEndPoint):
    _url = '/playlistItems'
    _methods = {
        'list': {
            'method': 'GET',
            'required': {
                'part': SET('id', 'snippet', 'contentDetails', 'status'),
            },
            'filter': {
                'id': str,
                'playlistId': str,
            },
            'optional': {
                'maxResults': INT,
                'onBehalfOfContentOwner': str,
                'pageToken': str,
                'videoId': str,
            },
        },
        'insert': {
            'method': 'POST',
            'required': {
                'part': SET('snippet', 'contentDetails', 'status'),
            },
            'optional': {
                'onBehalfOfContentOwner': str,
            },
        },
        'update': {
            'method': 'PUT',
            'required': {
                'part': SET('snippet', 'contentDetails', 'status'),
            },
        },
        'delete': {
            'method': 'DELETE',
            'required': {
                'id': str,
            },
        },
    }


class Search(GoogleApiEndPoint):
    _url = '/search'
    _methods = {
        'search': {
            'method': 'GET',
            'required': {
                'part': SET('snippet'),
            },
            'filter': {
                'forContentOwner': bool,
                'forDeveloper': bool,
                'forMine': bool,
                'relatedToVideoId': str,
            },
            'min_filters': 0,
            'optional': {
                'channelId': str,
                'channelType': SET('any', 'show'),
                'eventType': SET('completed', 'live', 'upcoming'),
                'location': str,
                'locationRadius': str,
                'maxResults': INT,
                'onBehalfOfContentOwner': str,
                'order': SET('date', 'rating', 'relevance', 'title', 'videoCount', 'viewCount'),
                'pageToken': str,
                'publishAfter': DATETIME,
                'publishedBefore': DATETIME,
                'q': str,
                'regionCode': str,
                'relevanceLanguage': str,
                'safeSearch': SET('moderate', 'none', 'strict'),
                'topicId': str,
                'type': SET('channel', 'playlist', 'video'),
                'videoCaption': SET('any', 'closedCaption', 'none'),
                'videoCategoryId': str,
                'videoDefinition': SET('any', 'high', 'standard'),
                'videoDimension': SET('2d', '3d', 'any'),
                'videoDuration': SET('any', 'long', 'medium', 'short'),
                'videoEmbeddable': SET('any', 'true'),
                'videoLicense': SET('any', 'creativeCommon', 'youtube'),
                'videoSyndicated': SET('any', 'true'),
                'videoType': SET('any', 'episode', 'movie'),
            },
        },
    }

    def __call__(self, *args, **kwargs):
        return self.search(*args, **kwargs)


class YoutubeV3(GoogleApi):
    _url = '/youtube/v3'
    _apis = {
        'playlists': Playlists,
        'playlistItems': PlaylistItems,
        'search': Search,
    }
