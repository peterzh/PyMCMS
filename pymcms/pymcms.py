import yaml


def handle_cli_arguments(args):
    """
    Handle CLI arguments
    """
    raise NotImplementedError


def load_config():
    """
    Parse ../config.yaml file
    """
    with open('../config.yaml', 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    return cfg


def post_weight(mouse_name, weight, date):
    """
    Post weight to MCMS for a given mouse_name, and date
    """
    raise NotImplementedError


def get_weight(mouse_name, date):
    """
    Get the mouse weight from MCMS for a given date
    """
    raise NotImplementedError


def get_weight_baseline(mouse_name):
    """
    Get mouse weight as a percentage of its baseline weight
    """
    raise NotImplementedError


def delete_weight(weight_record):
    """
    Delete MCMS weight record
    """
    raise NotImplementedError


def update_weight(weight_record, new_weight):
    """
    Update the MCMS weight record to a new weight
    """
    raise NotImplementedError


def get_mouse_names(colony_prefix):
    """
    Get list of mice from a given MCMS colony prefix
    """
    raise NotImplementedError


def create_gui():
    """
    Create GUI windows and buttons
    """
    raise NotImplementedError