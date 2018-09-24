# -*- coding: utf-8 -*-
# @File  : serializers.py
# @Author: KingJX
# @Date  : 2018/9/24 19:35
""""""
from rest_framework import serializers

from boker.models import Essay


class EssaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Essay
        fields = ['id', 'e_name', 'e_label', 'e_content', 'e_create_time', 'e_operate_time', 'is_delete', 'e_auth_id', 'e_part_id']


if __name__ == '__main__':
    pass
