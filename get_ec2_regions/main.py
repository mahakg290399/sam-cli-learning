import boto3
import json

ec2Client = boto3.client('ec2')

def lambda_handler(event, context):
    regionRes = ec2Client.describe_regions()
    return{
        "statusCode" : 200,
        "body": json.dumps({
            "message": regionRes['Regions']
        })
    }