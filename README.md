## TensorFlow GPU checker (in case I forgot)

A love letter to my future self, and also for the poor souls not being able to access their GPUs with the new version of `tensorflow`, that is 2.11.0 [(ref)](https://stackoverflow.com/questions/75249688/how-to-use-the-gpu-with-tensorflow-2-11), downgrade to version 2.10 and follow these steps:
1. Run `conda create -n tf_gpu`, activate it immediately
2. Run `pip install tensorflow==2.10`
3. Run this particular script:
```
$python verify_gpu.py
```

Should output something like:
![image](https://user-images.githubusercontent.com/62300057/221502688-aec621ce-5a28-4e12-aed4-9d3061624555.png)

