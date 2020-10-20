# pylint: disable=too-many-instance-attributes
import enum
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, TextIO, Tuple, Pattern


@dataclass
class GlobalOptions:
    json: bool
    rules: Tuple[TextIO, ...]
    ignore_rules: Tuple[TextIO, ...]
    ignore_paths: Optional[TextIO]
    default_regexes: bool
    entropy: bool
    regex: bool
    interactive: bool
    include_paths: Optional[TextIO]
    exclude_paths: Optional[TextIO]
    exclude_signatures: Tuple[str, ...]
    output_dir: Optional[str]
    git_rules_repo: Optional[str]
    git_rules_files: Tuple[str, ...]
    git_ignore_rules_files: Tuple[str, ...]
    config: Optional[TextIO]
    compact: bool = False


@dataclass
class GitOptions:
    since_commit: Optional[str]
    max_depth: int
    branch: Optional[str]


@dataclass
class FolderOptions:
    pattern: Optional[str] = "*"


class IssueType(enum.Enum):
    Entropy = "High Entropy"
    RegEx = "Regular Expression Match"


@dataclass
class Chunk:
    contents: str
    file_path: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Rule:
    name: Optional[str]
    pattern: Pattern
    path_pattern: Optional[Pattern]


class TartufoException(Exception):
    """Base class for all package exceptions"""


class ConfigException(TartufoException):
    """Raised if there is a problem with the configuration"""


class ScanException(TartufoException):
    """Raised if there is a problem encountered during a scan"""


class GitException(TartufoException):
    """Raised if there is a problem interacting with git"""


class GitLocalException(GitException):
    """Raised if there is an error interacting with a local git repository"""


class GitRemoteException(GitException):
    """Raised if there is an error interacting with a remote git repository"""
