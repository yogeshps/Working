import os
import sys

import constants
import openai

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY

query = sys.argv[1]

loader = TextLoader(r"C:\Users\Yogi\Desktop\Curiosa Academy\Clients\Kaliber\Code\Working\kaliber.py")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))
