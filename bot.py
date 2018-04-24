from piston.steem import Steem

steemPostingKey = os.environ.get('steemPostingKey')
steemAccountName = os.environ.get('steemAccountName')

steem = Steem(wif = steemPostingKey)
tagsOrAuthors = ["smartcash", "crypt0", "heiditravels", "jerrybanfield", "whiteblood", "scooter77", "ellemarieisme", "shayne", "maneco64"]
voteWeight = 50

for p in steem.stream_comments():
        for tag in tagsOrAuthors:
            try:
                # make p["tags"] into p["author"] if you are voting by author and not by tag
                if tag in p["author"] and p.is_main_post():
                    vote = p.upvote(weight = +voteWeight, voter = "your username here")
                    print("Upvoted post by @"+vote["operations"][0][1]["author"]+" using account @"+vote["operations"][0][1]["voter"]+"!")
            except:
                print("Failed to vote on post.")
