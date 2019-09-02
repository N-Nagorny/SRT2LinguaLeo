Just an initial dirty implementation of a Python script for getting a set of words from an SRT file that are marked in an LinguaLeo account as not fully learned.

Inspired by https://habr.com/post/276495/ and https://habr.com/post/345864/.

Tested with Python 3.5.2, can be run like:

python export.py <LinguaLeo_login> <LinguaLeo_pass> <srt_file> <file_for_export>

Uses https://pypi.org/project/srt/ for SRT parsing.
