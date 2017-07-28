import yaml
from plumbum import local
from pnldash_config import PROJECT_YML


def read_project_yml():
    with open(PROJECT_YML, 'r') as f:
        yml = yaml.load(f, Loader=yaml.loader.BaseLoader)
    required_keys = ['name', 'description']
    for required_key in required_keys:
        if not yml.get(required_key, None):
            raise Exception("'{}' missing required key: {}".format(
                PROJECT_YML, required_key))

    return yml
