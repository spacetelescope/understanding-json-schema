import os
from pathlib import Path
import sys

DEST_URL = "https://json-schema.org/understanding-json-schema/"

template = """
<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to {url}</title>
<meta http-equiv="refresh" content="0; URL={url}">
<link rel="canonical" href="{url}">
"""

source_path = Path(sys.argv[-1])
if not source_path.is_dir():
    raise ValueError(
        "Provide the source tree of HTML as the only argument")

dest_path = Path(__file__).parent

for html in source_path.glob('**/*.html'):
    relhtml = html.relative_to(source_path)
    url = DEST_URL + str(relhtml)
    desthtml = dest_path / relhtml

    if not desthtml.parent.is_dir():
        os.makedirs(desthtml.parent)

    with open(desthtml, 'w') as fd:
        fd.write(template.format(url=url))
