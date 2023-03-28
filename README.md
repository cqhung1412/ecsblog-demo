# ECS Blog Example

## Commands

```bash
# change the images in the docker-compose.yml file to the ones you want to use

# build the images with Docker Compose
docker compose build

# push the images
docker compose push

# create an ECS context, use AWS environment variables to authenticate
docker context create ecs myecscontext # or user/bin/local/docker context create ecs myecscontext

# export the AWS keys
export AWS_ACCESS_KEY=...
export AWS_SECRET_KEY=...

# use the context
docker context use myecscontext

# deploy the stack
docker compose up

# convert the stack to a CloudFormation template
docker compose convert > ecs-blog-example.yml

# check services' state
docker compose ps

# curl the service
curl ecsbl-LoadB-XXXXXXXX-nnnnnnn.us-east-1.elb.amazonaws.com:80

# view logs
docker compose logs

# terminate the stack
docker compose down
```
