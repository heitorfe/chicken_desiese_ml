from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.evaluation import Evaluation
from src.cnnClassifier import logger

class EvolutionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

STAGE_NAME = "Evaluation"

try: 
    logger.info("***********************")
    logger.info(f"<<<<<< stage {STAGE_NAME} started<<<<<<")
    model_evaluation = ModelTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e
