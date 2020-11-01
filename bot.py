from instapy import InstaPy


session = InstaPy(username="learn_earn_travel_enjoy", password="000000")
session.login()

session.like_by_tags(['саяхат', 'английский'], amount=6)

session.set_do_follow(True, percentage=25)

session.session.set_do_comment(True,percentage=50)
session.set_comments(['Love it','Nice post', u'Kushti 😍'])

session.end()
