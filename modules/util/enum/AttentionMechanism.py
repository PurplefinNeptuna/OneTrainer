from enum import Enum


class AttentionMechanism(Enum):
    DEFAULT = 'DEFAULT'
    XFORMERS = 'XFORMERS'
    SDP = 'SDP'
    SUB_QUAD = 'SUB_QUAD'

    def __str__(self):
        return self.value
