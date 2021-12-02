import requests
from pyquery import PyQuery

# write clan tag here
clanTag = "R2U902U"


ret = requests.get('https://clashratings.com/coc/clan/' + clanTag)

print(ret.url)

memberDict = {}
doc = PyQuery(ret.content)
clanName = doc("h2.clanHeader_name_coc").text()
clanName = "Clan Name: " + clanName.split(" ")[0]
clanWarLeague = doc("div.clanNameTag div.clanHeader_description div:nth-child(2)").text()
clanWarLeague = "War League : " + clanWarLeague.split(" ")[0] + clanWarLeague.split(" ")[1]
print(clanName)
print(clanTag)
print(clanWarLeague)

memberIdList = doc("tr.tableRow_clanRatings td.clanPlayerName p:nth-child(4)")
for memberId in memberIdList:
    ret = requests.get("https://clashratings.com/coc/player/" + memberId.text[1:] + "/army")
    docForMember = PyQuery(ret.content)
    playerName = docForMember("h2.playerHeader_name_coc.goldText").text()
    playerName = playerName.split(" ")[0]
    heroRow = docForMember("div.centerDiv>div.row:nth-child(1)")
    troopRow = docForMember("div.centerDiv>div.row:nth-child(2)")
    siegeRow = docForMember("div.centerDiv>div.row:nth-child(3)")
    petRow = docForMember("div.centerDiv>div.row:nth-child(5)")

    heroLevels = heroRow("div.coc_playerArmy p.coc_playerArmy_stats:last-child")
    if(heroLevels.length >= 1):
        barbKing = " 蛮王 " + heroLevels[0].text[6:8]
    if(heroLevels.length >= 2):
        queen = " 女王 " + heroLevels[1].text[6:8]
    if(heroLevels.length >= 3):
        warden = " 咏王 " + heroLevels[2].text[6:8]
    if(heroLevels.length >= 4):
        royale = " 闰土 " + heroLevels[3].text[6:8]
    print(playerName + barbKing + queen + warden + royale)



