# Sample documents
documents = [
    "Retrieval-Augmented Generation (RAG) combines information retrieval with text generation.",
    "The RAG  rag rag model first retrieves relevant documents and then generates a response.",
    "RAG is used in various applications such as chatbots and virtual assistants.",
    "Information retrieval techniques include TF-IDF and cosine similarity.",
    "Text generation models can be based on transformers, like GPT-3."
]

def tokenize(text):
    return text.lower().split()

def compute_tf(text):
    tokens = tokenize(text)
    tf = {}
    for token in tokens:
        tf[token] = tf.get(token, 0) + 1
    return tf

def compute_similarity(tf1, tf2):
    common_tokens = set(tf1.keys()) & set(tf2.keys())
    similarity = sum(min(tf1[token], tf2[token]) for token in common_tokens)
    return similarity

def retrieve_documents(query, documents, top_n=2):
    query_tf = compute_tf(query)
    doc_similarities = []
    for doc in documents:
        doc_tf = compute_tf(doc)
        similarity = compute_similarity(query_tf, doc_tf)
        doc_similarities.append((similarity, doc))
    doc_similarities.sort(reverse=True, key=lambda x: x[0])
    return [doc for _, doc in doc_similarities[:top_n]]

# Example query
query = "Explain the concept of RAG in AI."
retrieved_docs = retrieve_documents(query, documents)
print("Retrieved Documents:", retrieved_docs)
            
    
