#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Sample document filter."""

from __future__ import annotations
import typing
from dataclasses import dataclass, field

from ttconv.config import ModuleConfiguration
from ttconv.filters.document_filter import DocumentFilter
from ttconv.model import ContentDocument
import ttconv.style_properties as styles

@dataclass
class SETFONTSIZEFilterConfig(ModuleConfiguration):
  """Configuration class for the sample filter"""

  @classmethod
  def name(cls):
    return "setfontsize"

  font_size_pct: typing.Optional[int] = field(default=100)

class SETFONTSIZEFilter(DocumentFilter):
  """Sample filter"""

  @classmethod
  def get_config_class(cls) -> ModuleConfiguration:
    return SETFONTSIZEFilterConfig

  def __init__(self, config: SETFONTSIZEFilterConfig):
    super().__init__(config)

  def process(self, doc: ContentDocument):
    doc.get_body().set_style(
        styles.StyleProperties.FontSize,
        styles.LengthType(
          self.config.font_size_pct,
          styles.LengthType.Units.pct
        )
      )
