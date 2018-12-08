import service
import sys
import srt
import re

email = sys.argv[1]
password = sys.argv[2]
srt_file = sys.argv[3]
export_filename = sys.argv[4]

lingualeo = service.Lingualeo(email, password)
lingualeo.auth()

learned_words = lingualeo.get_all_words()
learned_words = [text.encode("utf8") for text in learned_words]

with open(srt_file, 'r') as myfile:
    srt_data=myfile.read()

subtitle_generator = srt.parse(srt_data);
subtitles = list(subtitle_generator)
srt_words = []
for subtitle in subtitles:
	wordList = re.sub("[^\w]", " ",  subtitle.content).split()
	srt_words.extend(wordList)
seen = set()
result = []
for item in srt_words:
    if item not in seen and item not in learned_words and len(item) > 1:
        seen.add(item)
        result.append(item)
with open(export_filename, 'w') as f:
    for item in seen:
        f.write("%s\n" % item)
