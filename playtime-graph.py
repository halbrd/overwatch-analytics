import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

username = "halbrd"
discriminator = "6804"
user_agent = "USER_AGENT"

r = requests.get("https://owapi.net/api/v3/u/{}-{}/blob".format(username, discriminator), headers={ "User-Agent": user_agent })

r = json.loads(r.text)

playtimes_comp = r["us"]["heroes"]["playtime"]["competitive"]
playtimes_qp = r["us"]["heroes"]["playtime"]["quickplay"]

playtimes_comb = {
    key: (playtimes_comp[key] if key in playtimes_comp else 0) + (playtimes_qp[key] if key in playtimes_qp else 0)
for key in set(playtimes_comp) | set(playtimes_qp)}

playtimes = pd.Series(playtimes_comb)
playtimes = playtimes.sort_values()

plt.figure(figsize=(10,4))
playtimes.plot(kind='barh')
plt.savefig("graph.png")
