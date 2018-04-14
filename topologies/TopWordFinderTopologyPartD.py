from streamparse import Grouping, Topology

from spouts.FileReaderSpout import FileReaderSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.NormalizerBolt import NormalizerBolt
from bolts.WordCountBolt import WordCountBolt
from bolts.TopNFinderBolt import TopNFinderBolt

class TopWordFinderTopologyPartC(Topology):
    config = {'coursera.datafile': 'resources/data.txt'}

    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # FileReaderSpout -> "spout"
    # SplitSentenceBolt -> "split"
    # WordCountBolt -> "count"
    # NormalizerBolt -> "normalize"
    # TopNFinderBolt -> "top-n"
    spout = FileReaderSpout.spec(name="spout")
    split = SplitSentenceBolt.spec(name="split", inputs=[spout])
    normalize = NormalizerBolt.spec(name="normalize", inputs=[split])
    count = WordCountBolt.spec(name="count", inputs={normalize: Grouping.fields("word")})
    top-n = TopNFinderBolt.spec(name="top-n", inputs=[count])

    # NOTE: will have to manually kill Topology after submission
