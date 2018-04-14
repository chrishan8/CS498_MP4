from streamparse import Grouping, Topology

from spouts.FileReaderSpout import FileReaderSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.WordCountBolt import WordCountBolt

class TopWordFinderTopologyPartA(Topology):
    config = {'coursera.datafile': 'resources/data.txt'}

    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # FileReaderSpout -> "spout"
    # SplitSentenceBolt -> "split"
    # WordCountBolt -> "count"
    spout = FileReaderSpout.spec(name="spout")
    split = SplitSentenceBolt.spec(name="split", inputs=[spout])
    count = WordCountBolt.spec(name="count", inputs={split: Grouping.fields("word")})

    # NOTE: will have to manually kill Topology after submission
