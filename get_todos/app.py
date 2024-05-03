# get_todos/app.py
import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TODOS_TABLE', 'todos')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    todos = table.scan()['Items']
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(todos)
    }
    return response