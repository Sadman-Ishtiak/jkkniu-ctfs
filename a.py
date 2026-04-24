a = """./jkkniuctf/aaa.gpr
./.git/COMMIT_EDITMSG
./README.md
./.git/HEAD
./jkkniuctf/secrete.txt
./.git/objects/a1/172fed60fef2f047a61e5d701967818eb7e167
./.git/refs/heads/main
./.git/refs/remotes/origin/main
./.git/objects/24/e8e8372af648101c5077c4271757a31a76474f
./jkkniuctf/aaa.rep/idata/~journal.bak
./jkkniuctf/aaa.rep/idata/~index.bak
./jkkniuctf/aaa.rep/user/~index.dat
./jkkniuctf/aaa.rep/versioned/~index.bak
./jkkniuctf/aaa.rep/versioned/~index.dat
./.git/description
./jkkniuctf/aaa.rep/idata/~index.dat
./.git/objects/43/2dda8c7224640bed8f77936aa8af56e5cab30f
./.git/index
./.git/logs/refs/remotes/origin/main
./jkkniuctf/aaa.rep/project.prp
./.git/hooks/post-update.sample
./.git/info/exclude
./.git/config
./.git/logs/refs/heads/main
./.git/hooks/pre-merge-commit.sample
./.git/hooks/pre-applypatch.sample
./.git/hooks/applypatch-msg.sample
./jkkniuctf/aaa.rep/idata/00/00000000.prp
./jkkniuctf/aaa.rep/projectState
./cipher.txt
./.git/hooks/pre-receive.sample
./.git/logs/HEAD
./story.py
./story.c
./.git/hooks/commit-msg.sample
./.git/hooks/pre-push.sample
./.git/hooks/prepare-commit-msg.sample
./.git/hooks/pre-commit.sample
./.git/hooks/sendemail-validate.sample
./.git/hooks/push-to-checkout.sample
./.git/hooks/update.sample
./.git/hooks/fsmonitor-watchman.sample
./.git/hooks/pre-rebase.sample
./jkkniuctf/typing_test_Sadman_1765279493474.pdf
./jkkniuctf/colors.png
./jkkniuctf/notification.webm
./chall
./jkkniuctf/chall
./jkkniuctf/mystery_qr (1).png
./jkkniuctf/mystery_qr (2).png
./jkkniuctf/mystery_qr.png
./crypto.png
./jkkniuctf/notification.mp3
./jkkniuctf/ShadowTrace.evtx
./c
./dress.jpg
./jkkniuctf/Top 10 Teams.png
./Find_me.7z
./network_capture.pcap
./Find_me.png
./jkkniuctf/L.png
./bullshit.js
./index-Bdq2J1BO.js
./jkkniuctf/osint.jpg
./jkkniuctf/Flag_Chai.pka
./Statue.jpg
./jkkniuctf/captive_bird.jpg
./jkkniuctf/stegano/captive_bird.jpg
./jkkniuctf/aaa.rep/idata/00/~00000000.db/db.1.gbf
./jkkniuctf/IMG_5455.HEIC
./EX!T.png
./EX1T.png
./jkkniuctf/Favourite_one.mp3
./jkkniuctf/video6179082363998313268.mp4
./jkkniuctf/CiscoPacketTracer_900_Ubuntu_64bit.deb"""

a = a.splitlines()
# print(a)
for i in a:
	print(f"git add {i[2:]}")
	print(f"git commit -m \"{i[2:]}\"")
	print("git push origin main")

