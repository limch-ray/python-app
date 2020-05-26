# To build this image with docker
```
docker build -t image_name:TAG .
```

# To run this via docker
```
docker run -itd -e REDIS_HOST=<REDIS HOSTNAME> -e REDIS_DB=<REDIS DB> -e REDIS_PORT=<REDIS PORT> -p 5000:5000 image_name:TAG
```
