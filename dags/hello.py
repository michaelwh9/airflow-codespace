#Import Module
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

#Define Function
def print_hello():
    return'Hello Golden Boy'

dag = DAG(dag_id='multiple_dag_mich',
        description='My first DAG with multiple task',
        schedule_interval='@hourly',
        start_date=datetime(2025,9,21),
        catchup=False)

#Define Task
task_start = DummyOperator(task_id='start', dag=dag)
task_hello = PythonOperator(task_id='hello', python_callable=print_hello, dag=dag)
task_end = DummyOperator(task_id='end', dag=dag)

# Define Dependency / Task Flow /Task Sequence
task_start >> task_hello >> task_end