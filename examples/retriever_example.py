import logging
from personal_graph import GraphDB, PersonalRM


def main():
    with GraphDB() as graph:
        query = "What is the similarity between Jack and Ronaldo?"
        retriever = PersonalRM(graph)

        passages = retriever.forward(query)

        logging.info("Retrieved Results: ")
        for passage in passages:
            logging.info(passage)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
    )

    main()
