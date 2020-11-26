from typing import List
import enum
import re
import textblob


def get_words(transcript):
    no_brackets = re.sub("[\(\[<].*?[\)\]>]", "", transcript)
    no_caps = no_brackets.lower()
    no_punctuation = re.sub('[.?",]|-{2,}', '', no_caps)
    return no_punctuation.split()


class TextComparator:
    """


    == Instance Attributes ==
    fullTranscript:
    editedTranscript:
    storytellerTranscript:
    mattTranscript:
    marishaTranscript:
    samTranscript:
    ashleyTranscript:
    liamTranscript:
    travisTranscript:
    lauraTranscript:
    taliesinTranscript:

    allWords: A list of all words said in all versions of the story, in order,
        with duplicates.
    storytellerWords: A list of all words said by the original storyteller in
        their version of the story, in order, with duplicates.
    mattWords: A list of all words said by Matthew Mercer in their version of
        the story, in order, with duplicates.
    marishaWords: A list of all words said by Marisha Ray in their version of
        the story, in order, with duplicates.
    samWords: A list of all words said by Sam Riegel in their version of the
        story, in order, with duplicates.
    ashleyWords: A list of all words said by Ashley Johnson in their version of
        the story, in order, with duplicates.
    liamWords: A list of all words said by Liam O'Brien in their version of the
        story, in order, with duplicates.
    travisWords: A list of all words said by Travis Willingham in their version
        of the story, in order, with duplicates.
    lauraWords: A list of all words said by Laura Bailey in their version of the
        story, in order, with duplicates.
    taliesinWords: A list of all words said by Taliesin Jaffe in their version
        of the story, in order, with duplicates.
    """
    fullTranscript: str
    editedTranscript: str
    storytellerTranscript: str
    mattTranscript: str
    marishaTranscript: str
    samTranscript: str
    ashleyTranscript: str
    liamTranscript: str
    travisTranscript: str
    lauraTranscript: str
    taliesinTranscript: str

    allWords: List[str]
    storytellerWords: List[str]
    mattWords: List[str]
    marishaWords: List[str]
    samWords: List[str]
    ashleyWords: List[str]
    liamWords: List[str]
    travisWords: List[str]
    lauraWords: List[str]
    taliesinWords: List[str]

    test: int

    def __init__(self, file):
        text = open(file, 'r')
        self.fullTranscript = text.read()

        speaker_indices = [['<MATT>', 0], ['<MARISHA>', 0], ['<SAM>', 0],
                           ['<ASHLEY>', 0], ['<LIAM>', 0], ['<TRAVIS>', 0],
                           ['<LAURA>', 0], ['<TALIESIN>', 0]]

        i = 0
        while i < len(speaker_indices):
            speaker_indices[i][1] = \
                self.fullTranscript.find(speaker_indices[i][0])
            i += 1

        speakers_sorted = sorted(speaker_indices,
                                 key=lambda speaker: speaker[1])

        self.storytellerTranscript = self.fullTranscript[:speakers_sorted[1][1]]

        speakers = 0
        for i in speakers_sorted:
            start = speakers_sorted[speakers][1]
            if speakers < len(speakers_sorted) - 1:
                end = speakers_sorted[speakers + 1][1]
            else:
                end = len(self.fullTranscript)
            if i[0] == '<MATT>':
                self.mattTranscript = self.fullTranscript[start:end]
            elif i[0] == '<MARISHA>':
                self.marishaTranscript = self.fullTranscript[start:end]
            elif i[0] == '<SAM>':
                self.samTranscript = self.fullTranscript[start:end]
            elif i[0] == '<ASHLEY>':
                self.ashleyTranscript = self.fullTranscript[start:end]
            elif i[0] == '<LIAM>':
                self.liamTranscript = self.fullTranscript[start:end]
            elif i[0] == '<TRAVIS>':
                self.travisTranscript = self.fullTranscript[start:end]
            elif i[0] == '<LAURA>':
                self.lauraTranscript = self.fullTranscript[start:end]
            elif i[0] == '<TALIESIN>':
                self.taliesinTranscript = self.fullTranscript[start:end]
            speakers += 1

        self.allWords = get_words(self.fullTranscript)
        self.storytellerWords = get_words(self.storytellerTranscript)
        self.ashleyWords = get_words(self.ashleyTranscript)
        self.mattWords = get_words(self.mattTranscript)
        self.marishaWords = get_words(self.marishaTranscript)
        self.samWords = get_words(self.samTranscript)
        self.liamWords = get_words(self.liamTranscript)
        self.travisWords = get_words(self.travisTranscript)
        self.lauraWords = get_words(self.lauraTranscript)
        self.taliesinWords = get_words(self.taliesinTranscript)


tC = TextComparator("Ep. 1_ Pumat's Stroll - Formatted.txt")
print(tC.lauraTranscript)
