import os

from htx import app, init_model_server
from ner.ner import TransformersBasedTagger, train_ner


init_model_server(
    # refer to class definition that inherits htx.BaseModel and implements load() and predict() methods
    create_model_func=TransformersBasedTagger,
    # training script that will be called within RQ
    train_script=train_ner,
    # name of the Redis queue
    redis_queue=os.environ.get('RQ_QUEUE_NAME', 'default'),
    # Redis host
    redis_host=os.environ.get('REDIS_HOST', 'localhost'),
    # here we pass the kwargs parameters to train script
    pretrained_model=os.environ.get('pretrained_model', 'bert-base-uncased'),
    cache_dir=os.environ.get('cache_dir', '/data/cache'),
    model_dir=os.environ.get('model_dir', '/data/model'),
)
