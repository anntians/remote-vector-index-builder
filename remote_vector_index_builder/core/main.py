from core.tasks import build_index
from core.common.models import VectorsDataset
from core.common.models import IndexBuildParameters
import numpy as np
import os
import logging
logger = logging.getLogger(__name__)

def test_data():

    start = int(os.environ.get("START", 1))
    end = int(os.environ.get("END", 1000000))

    for i in range (start,end):
        logger.info(f"Running for doc count {i}")
        np_vecs = np.array([[float(j) + 1 for j in range(5)] for _ in range(i)], dtype=np.float32)
        np_docs = np.arange(0, i, dtype=np.int32)

        vectors_dataset = VectorsDataset(vectors=np_vecs, doc_ids=np_docs)
        index_build_params = IndexBuildParameters(
            container_name="testbucket",
            vector_path="vec.knnvec",
            doc_id_path="doc.knndid",
            dimension=5,
            doc_count=i,
            repository_type="s3",
        )
        build_index(
            index_build_params=index_build_params,
            vectors_dataset=vectors_dataset,
            cpu_index_output_file_path=f"/remote_vector_index_builder/graph_files/graph_{i}.faiss"
        )
        logger.info(f"Built graph for vectors with doc count {i}")

def configure_logging(log_level):
    # Configure logging
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

if __name__ == "__main__":
    configure_logging("INFO")
    test_data()