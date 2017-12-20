from logging import Logger

from utils.parameter import AppConfig, ModelParameter

APP_CONFIG = AppConfig.load_config('settings/app.yaml')['debug']
MODEL_CONFIG = APP_CONFIG.model_parameter  # type: ModelParameter
LOGGER = APP_CONFIG.logger  # type: Logger
