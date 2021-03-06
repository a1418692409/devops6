# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from dashboard.models import UserProfile


class WorkOrder(models.Model):
    ORDER_TYPE = (
        (0, '数据库'),
        (1, 'WEB服务'),
        (2, '计划任务'),
        (3, '配置文件'),
        (4, '其它'),
    )
    STATUS = (
        (0, '申请'),
        (1, '处理中'),
        (2, '完成'),
        (3, '失败'),
    )
    title = models.CharField(max_length=100, verbose_name=u'工单标题')
    type = models.IntegerField(choices=ORDER_TYPE, default=0, verbose_name=u'工单类型')
    order_contents = models.TextField(verbose_name='工单内容')
    applicant = models.ForeignKey(UserProfile, verbose_name=u'申请人', related_name='work_order_applicant')
    assign_to = models.ForeignKey(UserProfile, verbose_name=u'指派给')
    status = models.IntegerField(choices=STATUS, default=0, verbose_name=u'工单状态')
    result_desc = models.TextField(verbose_name=u'处理结果', blank=True, null=True)
    apply_time = models.DateTimeField(auto_now_add=True, verbose_name=u'申请时间')
    complete_time = models.DateTimeField(auto_now=True, verbose_name=u'处理完成时间')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'work_order'
        verbose_name_plural = verbose_name
        ordering = ['-complete_time']


class  echarts_order(models.Model):
    uid  = models.CharField(max_length=10, verbose_name=u'提交人')
    web      = models.CharField(max_length=10, verbose_name=u'Web类型')
    db       = models.CharField(max_length=10, verbose_name=u'DB类型')
    crontab  = models.CharField(max_length=10, verbose_name=u'crontab类型')
    conf     = models.CharField(max_length=10, verbose_name=u'conf类型')
    other    = models.CharField(max_length=10, verbose_name=u'other类型')
    data_collection_time = models.CharField(max_length=10,verbose_name=u'数据收集时间')



