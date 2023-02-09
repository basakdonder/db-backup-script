import boto3
from boto.exception import S3ResponseError
import zipfile
from datetime import date

AWS_ACCESS_KEY_ID = "<access key id here>"
AWS_SECRET_ACCESS_KEY = "<secret access key here>"
AWS_STORAGE_BUCKET_NAME = "<bucket name here>"
AWS_S3_ENDPOINT_URL = "<s3 endpoint>"

AWS_S3_CREDS = {
    "aws_access_key_id": AWS_ACCESS_KEY_ID,
    "aws_secret_access_key": AWS_SECRET_ACCESS_KEY,
    "endpoint_url": AWS_S3_ENDPOINT_URL,
}

client = boto3.client("s3", **AWS_S3_CREDS)
today = str(date.today())

with zipfile.ZipFile("db_backup.zip", "w") as backup_zip:
    backup_zip.write("db.sqlite3")
    print(backup_zip.namelist())

try:
    client.upload_file("db_backup.zip", AWS_STORAGE_BUCKET_NAME, "db_backup_" + today + ".zip")
    print("Database archiving completed.")
except:
    S3ResponseError()
    # Handle errors returned from AWS here
