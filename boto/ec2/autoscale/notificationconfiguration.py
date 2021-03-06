# Copyright (c) 2009-2011 Reza Lotun http://reza.lotun.name/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

class NotificationConfiguration(object):
    def __init__(self, connection=None):
        self.connection = connection
        self.group_name = None
        self.notification_type = None
        self.topic_arn = None

    def __repr__(self):
        return 'NotificationConfiguration: For group:%s, notification type:%s, topic arn:%s' % (self.group_name,
                                                                      self.notification_type,
                                                                      self.topic_arn)

    def startElement(self, name, attrs, connection):
        return None

    def endElement(self, name, value, connection):
        if name == 'AutoScalingGroupName':
            self.group_name = value
        elif name == 'NotificationType':
            self.notification_type = value
        elif name == 'TopicARN':
            self.topic_arn = value
        else:
            setattr(self, name, value)

