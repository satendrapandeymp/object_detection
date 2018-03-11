Git link for pretrained mode --  
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

Look at time, accurecy trade-off and choose wisely.

Git link of tutorial, Clone and merge with tenserflow object_detection -- 
https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10

compile .proc file --
protoc --python_out=. .\object_detection\protos\*.proto

### Install 
python setup.py build
python setup.py install

### for labelling 
1) ```sudo apt-get install pyqt4-dev-tools```

2) ```pip install labelImg```

3) ```labelImg```

lable all of your Images from test and train folder.


### Generating tf records

```python xml_to_csv.py```

* Label in big size picture *

run resize.py , pandas_csv.py to change you labeling and Image appropriately

modify "class_text_to_int(row_label)" in generate_tfrecord.py

```python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record ```

```python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record```

### making labelMap

the changes you made in generate_tfrecord.py just copy json to 
labelmap.pbtxt and save in training folder.

### making .config file

from models/research/object_detection/samples/configs copy appropriate config file

modify that file and save into training folder

some modification -:
1) fine_tune_checkpoint : "C:/tensorflow1/models/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt"
2) input_path : "C:/tensorflow1/models/research/object_detection/train.record"
3) label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"
4) input_path : "C:/tensorflow1/models/research/object_detection/test.record"
5) label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"
7) num_examples using test images

### Running training
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config

### looking at progress
C:\tensorflow1\models\research\object_detection>tensorboard --logdir=training

### exporting Interference graph
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph

### Finally testing 

Object_detection_webcam.py
and edit NUM_CLASSES = 6
