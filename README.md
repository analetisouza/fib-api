## How to run

_**Attention**: Before proceeding, Docker must be installed and running on your machine._

After cloning the repository, open the `fib-api` folder on a terminal and run the following commands: 

```
docker build -t fib-api .
```

```
docker run -p 8000:8000 fib-api
```

```
curl -v -X 'GET' \
'http://0.0.0.0:8000/api/fibonacci' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"num_elements": 7
}'
```