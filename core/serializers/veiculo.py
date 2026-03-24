from rest_framework.serializers import ModelSerializer

from core.models import Veiculo


class Veiculoserializer(ModelSerializer):
    class Meta:
        modal = Veiculo
        fields = '__all__'

