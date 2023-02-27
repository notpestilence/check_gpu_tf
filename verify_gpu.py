from tensorflow.python.client import device_lib
# Tensorflow 2.10
def main():
    local_device_protos = device_lib.list_local_devices()
    print([x.physical_device_desc for x in local_device_protos if x.device_type == 'GPU'])

if __name__ == "__main__":
    main()