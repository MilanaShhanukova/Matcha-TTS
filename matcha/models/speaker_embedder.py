import torch
import torch.nn as nn
from speechbrain.inference.speaker import EncoderClassifier
from speechbrain.lobes.models.ECAPA_TDNN import ECAPA_TDNN
from speechbrain.lobes.features import Fbank
from speechbrain.processing.features import InputNormalization


class SpeakerEmbedder(nn.Module):
    def __init__(self, pretrained_path="speechbrain/spkrec-ecapa-voxceleb", fine_tune=True) -> None:
        super().__init__()
        # TODO: load from the hparams
        self.emb_model = ECAPA_TDNN(input_size=80,
                                channels=[1024, 1024, 1024, 1024, 3072],
                                kernel_sizes=[5, 3, 3, 3, 1],
                                attention_channels=128,
                                dilations=[1, 2, 3, 4, 1],
                                lin_neurons=192)
        self.preload_model()
    
    def preload_model(self, checkpoint_path="/home/milana/TTS/matcha/Matcha-TTS/spkrec-ecapa-voxceleb/embedding_model.ckpt"):
        weights = torch.load(checkpoint_path)

        self.emb_model.load_state_dict(weights)
    
    def forward(self, features: torch.tensor, wav_lengths=None):
        normalized_features = features
        embeddings = self.emb_model(normalized_features, wav_lengths)

        embeddings = embeddings.squeeze(1)
        return embeddings
