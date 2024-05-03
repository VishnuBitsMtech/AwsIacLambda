# create_todo/app.py
import json
import os
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TODOS_TABLE', 'todos')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    body = json.loads(event['body'])
    todo = {
        'id': str(uuid.uuid4()),
        'text': body['text'],
        'completed': False
    }
    table.put_item(Item=todo)
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(todo)
    }
    return response