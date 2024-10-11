import librosa
import matplotlib.pyplot as plt
import IPython.display as ipd


class AudioProc(object):
    def __init__(self):
        self.emotions = {
            1 : 'neutral',  2 : 'calm',
            3 : 'happy',  4 : 'sad',
            5 : 'angry',  6 : 'fearful',
            7 : 'disgust',  8 : 'surprised' 
        }

    def load(self, paths: list) -> list:
        try:
            self.paths = paths
            return [librosa.load(_) for _ in paths]

        except FileNotFoundError:
            raise e
            return

    def plot_one(self, x, sr, voice_path: str):
        label = self.emotions[int(voice_path.split('/')[-1].split('-')[2][1])]
        fig, (ax1, ax2) = plt.subplots(2, figsize=(14, 9), sharex=True)
        fig.tight_layout()
        ax1.set_title(f'Спектрограмма. Эмоция - {label}')

        librosa.display.waveshow(x, sr=sr, color='blue', ax=ax1)
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz', ax=ax2)
        ax1.set_xlabel('')

    def plot_many(self, voices: list):
        [self.plot_one(x, sr, p) for (x, sr), p in zip(voices, self.paths)]

    def get_voice_one(self, path):
        label = self.emotions[int(path.split('/')[-1].split('-')[2][1])]
        print(label)

        return ipd.Audio(path)

    def get_voice_many(self):
        [ipd.display(self.get_voice_one(path)) for path in self.paths]

