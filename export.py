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

with open(srt_file, 'r') as myfile:
    srt_data=myfile.read()

subtitle_generator = srt.parse(srt_data);
subtitles = list(subtitle_generator)
srt_words = []
seen = set()

with open(export_filename, 'w') as f:
	for subtitle in subtitles:
		wordList = re.sub("[^\w]", " ",  subtitle.content).split()
		for word in wordList:
			if word not in seen and word not in learned_words and len(word) > 2 and not word.isdigit():
				seen.add(word.lower())
				f.write("%s\n" % word)
				lingualeo.add_word(word, subtitle.content)
