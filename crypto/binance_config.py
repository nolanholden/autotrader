import json

_PERSONAL_KEYS_JSON_PATH  = 'binance_personal_keys.json'
_API_KEY_PROPERTY_NAME    = 'api_key'
_SECRET_KEY_PROPERTY_NAME = 'api_secret'

def load_api_keys():
  """
  Return personal Binance api_key, api_secret from local files
  """
  with open(_PERSONAL_KEYS_JSON_PATH, 'r') as f:
    config = json.loads(f.read())
    api_key = config[_API_KEY_PROPERTY_NAME]
    secret = config[_SECRET_KEY_PROPERTY_NAME]
    return api_key, secret
