import logging
from pathlib import Path
from typing import List, Tuple

from audiobook_generator.book_parsers.base_book_parser import BaseBookParser
from audiobook_generator.config.general_config import GeneralConfig

logger = logging.getLogger(__name__)


class SSMLBookParser(BaseBookParser):
    def __init__(self, config: GeneralConfig):
        super().__init__(config)
        with open(self.config.input_file, 'r', encoding='utf-8') as f:
            self.content = f.read()
        if not self.content.strip().startswith('<speak>'):
            logger.warning("Input file does not start with <speak>, may not be valid SSML.")

    def validate_config(self):
        if self.config.input_file is None:
            raise ValueError("SSML Parser: Input file cannot be empty")

    def get_book_title(self) -> str:
        return Path(self.config.input_file).stem

    def get_book_author(self) -> str:
        return "Unknown"

    def get_chapters(self, break_string) -> List[Tuple[str, str]]:
        title = self.get_book_title()
        return [(title, self.content)] 