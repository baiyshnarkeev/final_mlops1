import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/narkeev123/final_mlops1.mlflow")
dagshub.init(repo_owner='narkeev123', repo_name='final_mlops1', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
