# Copyright 2022 SereTOD Challenge Organizers
# Authors: Hao Peng (peng-h21@mails.tsinghua.edu.cn)
# Apache 2.0
import torch 
import transformers 

from transformers import BertModel, BertTokenizer, BertTokenizerFast ,AutoModel,AutoTokenizer
from transformers import RobertaModel, RobertaTokenizer, RobertaTokenizerFast
from transformers import T5ForConditionalGeneration, T5TokenizerFast
from roformer import RoFormerModel


def get_backbone(model_type, model_name_or_path, tokenizer_name, markers, new_tokens:list = []):
    # if model_type == "bert":
    #     model = BertModel.from_pretrained(model_name_or_path)
    #     tokenizer = BertTokenizerFast.from_pretrained(tokenizer_name, never_split=markers)
    # elif model_type == "roberta":
    #     model = RobertaModel.from_pretrained(model_name_or_path)
    #     tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_name, never_split=markers)
    # elif model_type == "t5":
    #     model = T5ForConditionalGeneration.from_pretrained(model_name_or_path)
    #     tokenizer = T5TokenizerFast.from_pretrained(tokenizer_name, never_split=markers)
    # else:
    #     raise ValueError("No such model. %s" % model_type)
    model = RoFormerModel.from_pretrained(model_name_or_path)
    if model_type == 'deberta':
        tokenizer=BertTokenizerFast.from_pretrained(tokenizer_name, never_split=markers)
    else:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, never_split=markers)
    
    for token in new_tokens:
        tokenizer.add_tokens(token, special_tokens = True)
    if len(new_tokens) > 0:
        model.resize_token_embeddings(len(tokenizer))

    config = model.config
    return model, tokenizer, config

