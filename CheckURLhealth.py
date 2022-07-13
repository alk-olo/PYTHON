def lambda_handler(event, context):
  websiteURL = ['https://example1.com','https://example2.com','https://example3.com']
  topicArnCode = 'arn:aws:sns:ap-southeast-1:123:sample'
  for x in websiteURL:
    print (x)
    r = requests.get(x,verify=False)
    print (r)
    if r.status_code == 200:
      print('Website is ALIVE!')
    else:
      sns_client = boto3.client('sns')
      sns_client.publish(
      TopicArn = topicArnCode,
      Subject = 'Website is not reachable ' + x,
      Message = 'Website: ' + x + ' is down\n')
      print('Website is DEAD!')
