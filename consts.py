#!/usr/bin/env python
# coding:utf-8
""" 
@author: nivic ybyang7
@license: Apache Licence 
@file: consts.py
@time: 2023/01/07
@contact: ybyang7@iflytek.com
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import os
from urllib.parse import urlparse

diff_model_map = {
    '256x256_diffusion_uncond': {'downloaded': False,
                                 'sha': 'a37c32fffd316cd494cf3f35b339936debdc1576dad13fe57c42399a5dbc78b1',
                                 'uri_list': [
                                     'https://openaipublic.blob.core.windows.net/diffusion/jul-2021/256x256_diffusion_uncond.pt',
                                     'https://www.dropbox.com/s/9tqnqo930mpnpcn/256x256_diffusion_uncond.pt']},
    '512x512_diffusion_uncond_finetune_008100': {'downloaded': False,
                                                 'sha': '9c111ab89e214862b76e1fa6a1b3f1d329b1a88281885943d2cdbe357ad57648',
                                                 'uri_list': [
                                                     'https://huggingface.co/lowlevelware/512x512_diffusion_unconditional_ImageNet/resolve/main/512x512_diffusion_uncond_finetune_008100.pt',
                                                     'https://the-eye.eu/public/AI/models/512x512_diffusion_unconditional_ImageNet/512x512_diffusion_uncond_finetune_008100.pt']},
    'portrait_generator_v001': {'downloaded': False,
                                'sha': 'b7e8c747af880d4480b6707006f1ace000b058dd0eac5bb13558ba3752d9b5b9', 'uri_list': [
            'https://huggingface.co/felipe3dartist/portrait_generator_v001/resolve/main/portrait_generator_v001_ema_0.9999_1MM.pt']},
    'pixelartdiffusion_expanded': {'downloaded': False,
                                   'sha': 'a73b40556634034bf43b5a716b531b46fb1ab890634d854f5bcbbef56838739a',
                                   'uri_list': [
                                       'https://huggingface.co/KaliYuga/PADexpanded/resolve/main/PADexpanded.pt']},
    'pixel_art_diffusion_hard_256': {'downloaded': False,
                                     'sha': 'be4a9de943ec06eef32c65a1008c60ad017723a4d35dc13169c66bb322234161',
                                     'uri_list': [
                                         'https://huggingface.co/KaliYuga/pixel_art_diffusion_hard_256/resolve/main/pixel_art_diffusion_hard_256.pt']},
    'pixel_art_diffusion_soft_256': {'downloaded': False,
                                     'sha': 'd321590e46b679bf6def1f1914b47c89e762c76f19ab3e3392c8ca07c791039c',
                                     'uri_list': [
                                         'https://huggingface.co/KaliYuga/pixel_art_diffusion_soft_256/resolve/main/pixel_art_diffusion_soft_256.pt']},
    'pixelartdiffusion4k': {'downloaded': False,
                            'sha': 'a1ba4f13f6dabb72b1064f15d8ae504d98d6192ad343572cc416deda7cccac30', 'uri_list': [
            'https://huggingface.co/KaliYuga/pixelartdiffusion4k/resolve/main/pixelartdiffusion4k.pt']},
    'watercolordiffusion_2': {'downloaded': False,
                              'sha': '49c281b6092c61c49b0f1f8da93af9b94be7e0c20c71e662e2aa26fee0e4b1a9', 'uri_list': [
            'https://huggingface.co/KaliYuga/watercolordiffusion_2/resolve/main/watercolordiffusion_2.pt']},
    'watercolordiffusion': {'downloaded': False,
                            'sha': 'a3e6522f0c8f278f90788298d66383b11ac763dd5e0d62f8252c962c23950bd6', 'uri_list': [
            'https://huggingface.co/KaliYuga/watercolordiffusion/resolve/main/watercolordiffusion.pt']},
    'PulpSciFiDiffusion': {'downloaded': False,
                           'sha': 'b79e62613b9f50b8a3173e5f61f0320c7dbb16efad42a92ec94d014f6e17337f', 'uri_list': [
            'https://huggingface.co/KaliYuga/PulpSciFiDiffusion/resolve/main/PulpSciFiDiffusion.pt']},
    'secondary': {'downloaded': False, 'sha': '983e3de6f95c88c81b2ca7ebb2c217933be1973b1ff058776b970f901584613a',
                  'uri_list': [
                      'https://huggingface.co/spaces/huggi/secondary_model_imagenet_2.pth/resolve/main/secondary_model_imagenet_2.pth',
                      'https://the-eye.eu/public/AI/models/v-diffusion/secondary_model_imagenet_2.pth',
                      'https://ipfs.pollinations.ai/ipfs/bafybeibaawhhk7fhyhvmm7x24zwwkeuocuizbqbcg5nqx64jq42j75rdiy/secondary_model_imagenet_2.pth']},
}


def get_model_filename(diffusion_model_name):
    model_uri = diff_model_map[diffusion_model_name]['uri_list'][0]
    model_filename = os.path.basename(urlparse(model_uri).path)
    return model_filename
