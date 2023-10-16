from argparse import ArgumentParser

def argument():
    args = ArgumentParser()
    args.add_argument("--mode", default="INFO", type=str,
                    help="Enter log level (Default: INFO)")
    args.add_argument("--log-file", default=None, type=str,
                    help="Enter log file (Default: None)")

    return args.parse_args()