SCAN_TEXT = """
**#LethalEliminator**
**➛ Commander** : `{}`
**➛ Target User** : {}
**➛ Reason** : `{}`
**➛ Crime Coefficient** : `Over 300`

: : **Scan  Processed Time  And Date**: `{}`
"""

HELP = """
**Here Is The Help Menu Of Invaded**:-

**➛ Rankusers Commands**:
`!telegraph`
`!scan`
`!revert`
`!proof`
`!stats`
`!whois`

**➛ Invaders Commands**:
`!rank`
`!eval`
`!sh`

`!format` - **To Get Correct Formatting Methods**
"""


SCAN_APPROVED = """
**#LethalEliminator**
**➛ Troop** : **{}**
**➛ Target User** : **{}**
**➛ Approved By** : **{}**
**➛ Reason** : `{}`
**➛ Crime Coefficient** : `Over 300`

: : **Scan Processed Time And Date**: `{}`
"""

SCAN_DISAPPROVED = """
**$REJECTED**
**Crime Coefficient:** `Under 100`
`Not A Target For Enforcement Action`
`The Trigger Will Be Locked`

**Note:- The Scan Disapproved Due To Not Proper Reason, Proof etc**
**:: Try Scanning Again With Proper Reason And Proof**
"""

REQUEST_SCAN = """
**$SCAN**
`{}` **Is Requesting a Cymatic Scan For** {}
**Scan Reason:** `{}`
**Proof Message:** `{}` 

: : **Scan Processed Time And Date**: `{}`
"""


#aasf update this da

STATS = """
**Here The Stats Of Invaded:-**

➛ `{}` **Troops**
➛ `{}` **Commanders**
➛ `{}` **Scanned Users**

**: : By @InvadedRobot**
"""

CHECK_TEXT = """
**Details Of Following User:-**
➛ **User Id**: `{}`
➛ **Reason**: `{}`

: : **Scan Processed Time And Date**: `{}`
"""

PM_START_TEXT = """
`Hello There I Am` `I⊃：INVΛ⊃≡⊃` `The Judgement Enforcing System`

**Invaded Analysis Report :-**
**➛ User:** {}
**➛ ID:** `{}`
**➛ Is Restricted:** `{}`
**➛ Status:** `{}`
"""

GROUP_START_TEXT = """
`Hello There I Am` `I⊃：INVΛ⊃≡⊃` `The Judgement Enforcing System`

**Invaded Analysis Report :-**
**➛ Group:** `{}`
**➛ ID:** `{}`
**➛ Members Count:** `{}`
**➛ Message Count:** `{}`
"""

FORMAT_TEXT = """
**Here Is The Help For Formatting:-**

**• Scan Formatting Example:**

**If You're Replying Someone To Scan:-**
➛ `/scan -r scammer` `(Reply To A User)`

**Else If You're Using Id To Scan Someone:-**
➛ `/scan -u 123456789 -r scammer` `(No Need To Reply To A User)`

**• Revert Formatting Example:**

**If You're Reverting Someone's Scan:-**
➛ `/revert` `(Reply To A User)`

**Else If You're Using Id To Revert Someone's Scan:-**
➛ `/revert -u 123456789` `(No Need To Reply To A User)`

**• Adding Proof Formatting Example:**

➛ `/proof -u 123456789` `(Reply To A Media Ex:- (Photo, Document, Video (Under 6Mb)))`

**• Whois Formatting Example:**

**If You're Replying Someone To Get Info About Them:-**
➛ `/whois` `(Reply To A User)`

**Else If You're Using Id To Get Info About Someone:-**
➛ `/whois -u 123456789` `(No Need To Reply To A User)`

`: : Powered By Invaders`
"""

ANI0 = "`[▒▒▒▒▒▒▒▒▒▒▒▒▒▒]` `0%`"
ANI1 = "`[████▒▒▒▒▒▒▒▒▒▒]` `20%`"
ANI2 = "`[██████▒▒▒▒▒▒▒▒]` `40%`"
ANI3 = "`[████████▒▒▒▒▒▒]` `60%`"
ANI4 = "`[██████████▒▒▒▒]` `80%`"
ANI5 = "`[███████████████]` `100%`"
ANI6 = "`[COMPLETED]`"
