from instapy import InstaPy

session = InstaPy(username="dev_meyo", password="bontusfavor1994?")
session.login()
session.like_by_tags(["Python3", "Javascript", "Python Language", "Programming", "Coding"],
                     amount=5)
session.set_dont_like(["naked", "nsfw", "porn"])
session.set_do_follow(True, percentage=5)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "I love it", "Wow!", "Beautiful :heart_eyes:"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.set_relationship_bounds(enabled=True, max_followers=5000, min_followers=1000)
session.set_skip_users(skip_private=True, private_percentage=100, skip_no_profile_pic=True,
                       no_profile_pic_percentage=100)
session.set_skip_users(skip_private=True, skip_no_profile_pic=True, skip_business=True,
                       skip_business_categories=['Community', 'Creators & Celebrities',
                                                 'company', 'Community Organization'])
session.set_delimit_liking(enabled=True, max_likes=5000, min_likes=500)
session.set_delimit_commenting(enabled=True, max_comments=50, min_comments=0)
session.unfollow_users(amount=50, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60,
                       sleep_delay=655)
session.accept_follow_requests(amount=100, sleep_delay=5)

session.end()
