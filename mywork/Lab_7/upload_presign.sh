#!/bin/bash

FILE_NAME=$1
BUCKET_NAME=$2
EXPIRATION_TIME=$3
aws s3 cp $FILE_NAME s3://$BUCKET_NAME/
aws s3 presign --expires-in 30 s3://ds2002-mqx4vk/$FILE_NAME
# PRESIGNED_URL=$(aws s3 presign s3://$BUCKET_NAME/$(basename $LOCAL_FILE) --expires-in $EXPIRATION_TIME)
# echo "Presigned URL (expires in $EXPIRATION_TIME seconds):"
# echo $PRESIGNED_URL