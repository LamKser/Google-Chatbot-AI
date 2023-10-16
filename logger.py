import logging

from configs.color import ColorCode
from configs.format import FormatLogging


class CustomFormatter(logging.Formatter):

    FORMATS = {
        logging.DEBUG: "[{0}{1}{2}] {3}{4}".format(ColorCode.GREY, FormatLogging.LEVELNAME, ColorCode.RESET, FormatLogging.MESSAGE, ColorCode.RESET),
        logging.INFO: "[{0}{1}{2}] {3}{4}".format(ColorCode.GREEN, FormatLogging.LEVELNAME, ColorCode.RESET, FormatLogging.MESSAGE, ColorCode.RESET),
        logging.WARNING: "[{0}{1}{2}] {3}{4}".format(ColorCode.YELLOW, FormatLogging.LEVELNAME, ColorCode.RESET, FormatLogging.MESSAGE, ColorCode.RESET),
        logging.ERROR: "[{0}{1}{2}] {3}{4}".format(ColorCode.RED, FormatLogging.LEVELNAME, ColorCode.RESET, FormatLogging.MESSAGE, ColorCode.RESET),
        logging.CRITICAL: "[{0}{1}{2}] {3}{4}".format(ColorCode.BOLD_RED, FormatLogging.LEVELNAME, ColorCode.RESET, FormatLogging.MESSAGE, ColorCode.RESET),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def init_logger(log_file=None, name="Chat_bot", mode='INFO'):
    if mode == 'INFO':
        log_level = logging.INFO
    if mode == 'DEBUG':
        log_level = logging.DEBUG

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)

    if log_file:
        file_handler = logging.FileHandler(log_file, 'w')
        file_handler.setFormatter(CustomFormatter())
        file_handler.setLevel(log_level)
        logger.addHandler(file_handler)
    return logger