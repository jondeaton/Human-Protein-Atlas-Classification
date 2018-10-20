#!/usr/bin/env python
"""
File: config.py
Date: 10/19/18 
Author: Jon Deaton (jdeaton@stanford.edu)
"""
import os
import configparser

dir_name = os.path.dirname(__file__)
default_config_file = os.path.join(dir_name, "config_local.ini")

class Configuration(object):

    def __init__(self, config_file=default_config_file):

        assert isinstance(config_file, str)
        # Setup the filesystem configuration
        self._config_file = os.path.join(config_file)
        self._config = configparser.ConfigParser()
        self._config.read(self._config_file)
        c = self._config

        self.dataset_directory = os.path.expanduser(c["Data"]["path"])
        self.tfrecords_dir = os.path.expanduser(c["Data"]["TFRecords"])
        self.model_file = os.path.expanduser(c["Output"]["save-file"])

        self.tensorboard_dir = os.path.expanduser(c["TensorFlow"]["tensorboard-dir"])
        self.tensorboard_freq = int(c["TensorFlow"]["log-frequency"])

    def overload(self, args):
        assert args is not None

        if args.brats_directory is not None:
            self.dataset_directory = args.input_directory

        if args.model_file is not None:
            self.model_file = args.model_file

        if args.tensorboard is not None:
            self.tensorboard_dir = args.tensorboard