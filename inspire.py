import requests
import arxiv

# Define the base URL for the INSPIRE-HEP API
base_url = 'https://inspirehep.net/api/'

# Define the endpoint you want to access
endpoint = 'literature'

# Define the parameters for your API request
params = {
    'q': 'a Kaze W. K. Wong',  # Replace with the author's name you want to search for
    'size': 20,                # Replace with the number of results you want
    'format': 'json'           # Response format (JSON or XML)
}

# Send a GET request to the API
response = requests.get(base_url + endpoint, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the response content
    data = response.json()

    # Process the retrieved data
    for result in data['hits']['hits']:
        # Access individual fields
        title = result['metadata']['titles'][0]['title']
        authors = [author['full_name'] for author in result['metadata']['authors']]
        abstract = result['metadata']['abstracts']
        preprint = result['metadata']['arxiv_eprints']

        # Print the results
        print("Title:", title)
        print("Authors:", ", ".join(authors))
        print("Abstract:", abstract)
        print("Preprint:", preprint)
        print("---")

else:
    print("Error:", response.status_code)

def fetch_arxiv_pdf(id: str, directory="./local_workspace"):
    """Fetches an arXiv PDF file to a local directory.

    Args:
        id (str): arXiv ID of the paper.
        directory (str, optional): Local directory to save the PDF file. Defaults to "./local_workspace".
    """
    paper = next(arxiv.Search(id_list=[id]).results())
    paper.download_pdf(dirpath=directory, filename=id+".pdf")
    print(f"PDF file saved to {directory}/{id}.pdf")


from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

from paperqa.contrib import ZoteroDB
from paperqa import Docs

model = ChatOpenAI()
embeddings = OpenAIEmbeddings()

docs = Docs(llm=model, embeddings=embeddings)

docs.add("./local_workspace/2302.05333.pdf")
docs.add("./local_workspace/2302.05329.pdf")
docs.add("./local_workspace/2211.06397.pdf")
ans = docs.query("Find 5 references related to gravitational wave parameter estimation.")

