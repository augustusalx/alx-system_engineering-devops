#!/usr/bin/python3
"""
It queries the Reddit API and returns the number of subscribers aside active users,
total subscribers for a given subreddit. If an invalid subreddit is given,
return 0
"""
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    r_subreddit = get('http://www.reddit.com/r/{}/about.json'.
                      format(subreddit), headers={'User-Agent': 'Mybot'})
    try:
        subreddit_dict = r_subreddit.json()
        return subreddit_dict['data']['subscribers']
    except:
        return 0
