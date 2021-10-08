import urllib.request
import json


def get_total():
    urls = ["https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Spectrum%20Case",
            "https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Clutch%20Case",
            "https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Spectrum"
            "%202%20Case",
            "https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Falchion%20Case",
            "https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Danger%20Zone"
            "%20Case",
            "https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name=Prisma%20Case"]
    amount = [1519, 1108, 2000, 496, 772, 1000]
    single = []
    buy_price = [203.16, 44.32, 80, 64.96, 40.06, 40]
    development_absolute = []
    development_percentage = []
    asset = []
    dev_abs = []
    hash_name = []
    i = 0
    while len(urls) > i:
        with urllib.request.urlopen(urls[i]) as url:
            data = json.loads(url.read().decode())
            result = str(data["lowest_price"])
            result = result.replace("€", "")
            result = result.replace(",", ".")
            result = round(float(result), 2)
            single.append(result)
            hash_names = urls[i]
            hash_names = hash_names.replace("https://steamcommunity.com/market/priceoverview/"
                                            "?currency=3&appid=730&market_hash_name=", "")
            hash_names = hash_names.replace("%20", "")
            hash_names = hash_names.replace("Case", "")
            if len(hash_names) > 15:
                hash_names = hash_names[:5]
            if len(hash_names) < 15:
                rest = 15 - len(hash_names)
                hash_names = hash_names.ljust(rest)
            hash_name.append(hash_names)
            asset.append(single[i] * amount[i])
        i += 1
    get_total.total = 0
    total_old = 0
    i = 0
    while len(urls) > i:
        get_total.total = get_total.total + asset[i]
        total_old = total_old + buy_price[i]
        i += 1
    performance = round(((get_total.total / total_old) - 1) * 100)
    if performance > 0:
        performance = "+" + str(performance)
    performance = str(performance) + "%"
    print("Total of\t\t", round(get_total.total, 2), "€  \t Performance \t", performance)
    i = 0
    print("CASE", "\t\t\t", "ASSET", "\t\t\t", "SINGLE", "\t",
          "ALLOCATION")
    while len(asset) > i:
        development_absolute.append(round(asset[i] - buy_price[i], 2))
        if development_absolute[i] > 0:
            dev_abs = "+" + str(development_absolute[i])
        elif development_absolute[i] < 0:
            dev_abs = str(development_absolute[i])
        else:
            dev_abs = str(dev_abs)
        development_percentage.append(round(((asset[i] / buy_price[i]) - 1) * 100))
        if development_percentage[i] > 0:
            dev_per = "+" + str(development_percentage[i])
        elif development_absolute[i] < 0:
            dev_per = str(development_percentage[i])
        else:
            dev_per = str(development_percentage[i])
        print(hash_name[i], "\t\t", format(round(asset[i], 2), '.2f'), "€\t\t", single[i], "€\t\t",
              round((asset[i] / get_total.total * 100), 2), "%  \t\t", dev_abs, "€ \t\t", dev_per, "%")
        i += 1


get_total()
