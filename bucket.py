import boto3


### add the bucket as per your need
def addBucket(name,location='eu-west-3'):
    client = boto3.client(
    's3',
        aws_access_key_id=AC,
        aws_secret_access_key=AK
    )

    response = client.create_bucket(
        Bucket=name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-3',
        },
    )

    print (response)