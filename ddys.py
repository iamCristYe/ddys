src = [
    {"src":"javascript:;","src0":"\/v\/documentary\/MH370_The_Plane_That_Disappeared\/MH370_The_Plane_That_Disappeared_S01E01.mp4","src1":"nS2miQwEhgImy3R8UI5aESjjngAC7u8CzRcdcOWP94llBScv6BN8%2BRn1KF7u57YD%2Bkyzu6qoGT%2BYAsZxU%2FjM5s1TFUcLtLrEmQY7OkjjpwU%3D","src2":"tebVzRfOmuNOE","src3":"","title":"","type":"video\/mp4","caption":"\u98de\u884c\u5458","description":"","image":{"src":"https:\/\/ddys.art\/wp-includes\/images\/media\/video.png","width":48,"height":64},"thumb":{"src":"https:\/\/ddys.art\/wp-includes\/images\/media\/video.png","width":48,"height":64},"meta":{"length_formatted":""},"portn":"9543","srctype":"0","cut":"0","vttshift":"0","userIP":"61.145.25.119","subsrc":"\/v\/documentary\/MH370_The_Plane_That_Disappeared\/MH370_The_Plane_That_Disappeared_S01E01.ddr","dimensions":{"original":{"width":"300","height":"200"},"resized":{"width":"600","height":"400"}}},
{"src":"javascript:;","src0":"\/v\/documentary\/MH370_The_Plane_That_Disappeared\/MH370_The_Plane_That_Disappeared_S01E02.mp4","src1":"nS2miQwEhgImy3R8UI5aEaFJY5khbRJMavZ15blUVF2IOfbk5vZfaf5oBQV3Mo%2B4olUUvUUuUM3NULNbeShtVXqQonCOBxQ0k1aYZ5kZaw8%3D","src2":"tebVzRfOmuNOE","src3":"","title":"","type":"video\/mp4","caption":"\u52ab\u673a","description":"","image":{"src":"https:\/\/ddys.art\/wp-includes\/images\/media\/video.png","width":48,"height":64},"thumb":{"src":"https:\/\/ddys.art\/wp-includes\/images\/media\/video.png","width":48,"height":64},"meta":{"length_formatted":""},"portn":"9543","srctype":"0","cut":"0","vttshift":"0","userIP":"61.145.25.119","subsrc":"\/v\/documentary\/MH370_The_Plane_That_Disappeared\/MH370_The_Plane_That_Disappeared_S01E02.ddr","dimensions":{"original":{"width":"300","height":"200"},"resized":{"width":"600","height":"400"}}},
{"src":"javascript:;","src0":"\/v\/documentary\/MH370_The_Plane_That_Disappeared\/MH370_The_Plane_That_Disappeared_S01E03.mp4","src1":"nS2miQwEhgImy3R8UI5aEfRZVxoowpbz68iCQc%2Fhk2%2BxM3pjxtLseoMeWIaLMkTgR3ShCyexs20PNaA6LBXQwRd9SwHdNsX2axJE5XyuJDs%3D","src2":"tebVzRfOmuNOE","src3":"","title":"","type":"video\/mp4","caption":"\u62e6\u622a","description":"","image":{"src":"https:\/\/ddys.art\/wp-includes\/images\/media\/video.png","width":48,"height":64},"thumb":{"src":"https:\/\/ddys.art\/wp-includes\/images\/media\/video.png","width":48,"height":64},"meta":{"length_formatted":""},"portn":"9543","srctype":"0","cut":"0","vttshift":"0","userIP":"61.145.25.119","subsrc":"\/v\/documentary\/MH370_The_Plane_That_Disappeared\/MH370_The_Plane_That_Disappeared_S01E03.ddr","dimensions":{"original":{"width":"300","height":"200"},"resized":{"width":"600","height":"400"}}}

]


# print(src)
import os
import subprocess
import json

# curl 'https://ddys.art/getvddr/video?id=nS2miQwEhgImy3R8UI5aEYgalSoOTsyZXW8rXtCj7od9UVmbP%2Fibuc4%2Bs9KZV8HQgQtEutI6fuxXYCEc%2FqEPPQ%3D%3D&dim=1080P&type=mix'    -H 'cookie: X_CACHE_KEY=70cd25512b9c097aba396a664202f71f; __cf_bm=F.i_uXxXqERfXe.4XyatCauz11VWS7D.zshRwZYDxd8-1680496844-0-ASnRgrUzC5EBpmEA0yFpGA7JnmFChQa3eRajnPz8/s9/TsOsEOdAzNbwm+4JTQaVPgq6ns+csZR23Vvolqk/AW8rkguBbJdK7Ds0MHDbHavBH6F8Ak7BcBpQg6q7zHCy3g=='   -H 'referer: https://ddys.art/the-night-agent/?ep=6'

for entry in src:
    # curl = f"curl    -H 'authority: ddys.art'   -H 'accept: */*'   -H 'accept-language: ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7'   -H 'cookie: X_CACHE_KEY=70cd25512b9c097aba396a664202f71f; __cf_bm=O_5H5kCfM1NwpxRKK7QgkGs3QE4_kwLtsvTvobtmMg8-1680487478-0-AWmGUINi/h+Q7+25XWVF1d4S5aD/32LNPgLVNZ1tMYTFtGwDmpNf8TUcu7wRv+po+9dBQpM+QKHGtifb6cxulpvsDkTbuRROqF6spuR5vsVSbJo3ULX3LkDit4gI4CQURQ=='   -H 'dnt: 1'   -H 'referer: https://ddys.art/the-night-agent/?ep=2'   -H 'sec-ch-ua: \"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"'   -H 'sec-ch-ua-mobile: ?0'   -H 'sec-ch-ua-platform: \"Windows\"'   -H 'sec-fetch-dest: empty'   -H 'sec-fetch-mode: cors'   -H 'sec-fetch-site: same-origin'   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'"
    # os.system(curl)
    # subprocess.run(curl, capture_output=True)

    result = subprocess.run(
        [
            "curl",
            f"https://ddys.art/getvddr/video?id={entry['src1']}&dim=1080P&type=mix",
            "-H",
            "cookie:X_CACHE_KEY=70cd25512b9c097aba396a664202f71f;__cf_bm=F.i_uXxXqERfXe.4XyatCauz11VWS7D.zshRwZYDxd8-1680496844-0-ASnRgrUzC5EBpmEA0yFpGA7JnmFChQa3eRajnPz8/s9/TsOsEOdAzNbwm+4JTQaVPgq6ns+csZR23Vvolqk/AW8rkguBbJdK7Ds0MHDbHavBH6F8Ak7BcBpQg6q7zHCy3g==",
            "-H",
            "referer:https://ddys.art/the-night-agent/?ep=10",
        ],
        stdout=subprocess.PIPE,
    )
    temp = json.loads(result.stdout.decode("utf-8"))
    print(temp["url"])
    subprocess.run(["curl", temp["url"], "-o", entry["src0"][-43:]])
    os.system("sleep 10")
