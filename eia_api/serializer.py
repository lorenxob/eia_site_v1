from rest_framework import serializers

class DotSerializer(serializers.Serializer):
    value=serializers.FloatField()
    units=serializers.CharField()