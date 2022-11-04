import logging

LOG_LEVEL = 'DEBUG'  # Usually imported from parser or config file

def logger_config():
    # Gets or creates a logger
    logger = logging.getLogger(__name__)

    # set log level
    logger.setLevel(LOG_LEVEL)

    # define file handler and set formatter
    file_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%Y-%m-%d  %H-%M-%S')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)

    return logger


if __name__=='__main__':
  logger = logger_config()
  logger.info('this is an info log')
  logger.debug('this is an info log')

   
