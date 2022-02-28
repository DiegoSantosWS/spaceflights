"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from sqlalchemy import func

from .nodes import evaluate_model, split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
       
    pipeline_instance = pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                name="evaluate_model_node",
                outputs="metrics",
            ),
            # node(
            #     func=compare_shuttle_speed,
            #     inputs="shuttle_speed_data",
            #     outputs="shuttle_speed_comparison_plot",
            # ),
        ]
    )
    
    ds_pipeline_one = pipeline(
        pipe=pipeline_instance,
        inputs="model_input_table",
        namespace="active_modelling_pipeline",
    )
    
    ds_pipeline_two = pipeline(
        pipe=pipeline_instance,
        inputs="model_input_table",
        namespace="candidate_modelling_pipeline",
        parameters={"params:model_options": "params:model_options_experimental"},
    )
    
    return pipeline(
        pipe=ds_pipeline_one + ds_pipeline_two,
        inputs="model_input_table",
        namespace="data_science",
    )
    
