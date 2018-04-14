from streamparse import Grouping, Topology

from spouts.FileReaderSpout import FileReaderSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.NormalizerBolt import NormalizerBolt
from bolts.WordCountBolt import WordCountBolt

class TopWordFinderTopologyPartC(Topology):
    config = {'coursera.datafile': 'resources/data.txt'}

    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # FileReaderSpout -> "spout"
    # SplitSentenceBolt -> "split"
    # WordCountBolt -> "count"
    # NormalizerBolt -> "normalize"
    spout = FileReaderSpout.spec(name="spout")
    split = SplitSentenceBolt.spec(name="split", inputs=[spout])
    normalize = NormalizerBolt.spec(name="normalize", inputs=[split])
    count = WordCountBolt.spec(name="count", inputs={normalize: Grouping.fields("word")})

    # NOTE: will have to manually kill Topology after submission
