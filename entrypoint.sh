#!/bin/bash

# Stop and exit if any background process fail
set -e

# enable virtual environment
source ./venv/bin/activate

if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
  echo 'Running in Local'
  /usr/bin/aws-lambda-rie python -m awslambdaric "$1"
else
  echo 'Running in AWS'
  python -m awslambdaric "$1"
fi
