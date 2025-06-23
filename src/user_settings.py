# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://t.me/s/ConfigsHubPlus",
    "https://t.me/s/ShadowProxy66",
    "https://t.me/s/Hope_Net",
    "https://t.me/s/v2ray_configs_pool",
    #"https://t.me/s/IP_CF_Config",
    #"https://t.me/s/prrofile_purple",
    #"https://t.me/s/meli_proxyy",
    #"https://t.me/s/DirectVPN",
    #"https://t.me/s/moftconfig",
    #"https://t.me/s/proxyiranip",
    #"https://t.me/s/v2nodes",
    #"https://t.me/s/grizzlyvpn",
    #"https://t.me/s/v2ray_extractor",
    #"https://t.me/s/v2ray_configs_pool",
    #"https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt",
     "https://raw.githubusercontent.com/alirezaazarnoosh/LOG/refs/heads/main/README.md",
     "https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html",
     "https://raw.githubusercontent.com/alirezaazarnoosh/LOG/refs/heads/main/subshadmanegi",
     "https://raw.githubusercontent.com/miladtahanian/V2RayCFGDumper/main/config.txt",
    # "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/hysteria", 
    #"https://raw.githubusercontent.com/4n0nymou3/ss-config-updater/refs/heads/main/configs.txt",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = False

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 500

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": False,
    "ss://": True,
    "trojan://": False,
    "tuic://": False,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 3
