"""Project pipelines."""
import logging
from typing import Dict

from kedro.pipeline import Pipeline
from spaceflights.pipelines import data_processing as dp
from spaceflights.pipelines import data_science as ds


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    
    log = logging.getLogger(__name__)
    log.info("Start register_pipelines\n\r")
    
    data_processing_pipeline = dp.create_pipeline()
    
    log.info("create pipeline done\n\r") 
    
    log.info("Start register_pipelines ds \n\r")
    data_science_pipeline = ds.create_pipeline()
    
    log.info("create pipeline ds done\n\r") 
    
    
    
    return {
        "__default__": data_processing_pipeline + data_science_pipeline,
        "dp":data_processing_pipeline,
        "ds": data_science_pipeline,
    }
