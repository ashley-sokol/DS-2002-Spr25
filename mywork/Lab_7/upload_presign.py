import boto3
import urllib.request
import os
from urllib.parse import urlparse

s3 = boto3.client('s3', region_name='us-east-1')

def fetch_and_upload_file(url, bucket_name, expires_in):
    filename = os.path.basename(urlparse(url).path)
    urllib.request.urlretrieve(url, filename)
    with open(filename, 'rb') as data:
        s3.put_object(Body=data, Bucket=bucket_name, Key=filename)

    response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': filename},
    ExpiresIn=expires_in
)
    print(f"Presigned URL: {response}")
    return presigned_url