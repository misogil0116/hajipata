# 標準化
# データはirisデータセット
from common import load_iris, plot_scatter
import numpy as np
import matplotlib.pyplot as plt

def plot(setosa, versicolour, virginica, path):
  # before_normalization
  plt.clf()
  plot_scatter(setosa, marker='.', color='red')
  plot_scatter(versicolour, marker='o', color='blue')
  plot_scatter(virginica, marker='^', color='green')
  plt.title('あやめデータ')
  plt.xlabel('花弁の長さ')
  plt.ylabel('花弁の幅')
  plt.savefig(path)

if __name__ == "__main__":
  setosa, versicolour, virginica = load_iris()
  plot(setosa, versicolour, virginica, "results/original.png")

  setosa_N = len(setosa)
  versicolour_N = len(versicolour)
  virginica_N = len(virginica)

  all_data = np.array(setosa + versicolour + virginica, dtype=np.float32)
  N = all_data.shape[0]

  length, width = all_data[:, 0], all_data[:, 1]
  mu_l, mu_w = np.mean(length), np.mean(width)
  mu = np.array([mu_l, mu_w], dtype=np.float32)
  sigma_ll = (1/N) * np.sum((length - mu_l)**2)
  sigma_lw = (1/N) * np.sum((length - mu_l)*(width - mu_w))
  sigma_ww = (1/N) * np.sum((width - mu_w)**2)

  # normalization
  n_length = (length - mu_l) / np.sqrt(sigma_ll)
  n_width = (width - mu_w) / np.sqrt(sigma_ww)

  setosa = np.concatenate((n_length[:setosa_N], n_width[:setosa_N])).reshape(setosa_N, 2)
  versicolour = np.concatenate((n_length[setosa_N:setosa_N+versicolour_N], n_width[setosa_N:setosa_N+versicolour_N])).reshape(versicolour_N, 2)
  virginica = np.concatenate((n_length[setosa_N+versicolour_N:], n_width[setosa_N+versicolour_N:])).reshape(virginica_N, 2)
  
  # plot
  plt.clf()
  plt.scatter(setosa[:, 0], setosa[:, 1], marker='.', color='red')
  plt.scatter(versicolour[:, 0], versicolour[:, 1], marker='o', color='blue')
  plt.scatter(virginica[:, 0], virginica[:, 1], marker='^', color='green')
  plt.title('あやめデータ')
  plt.xlabel('花弁の長さ')
  plt.ylabel('花弁の幅')
  plt.savefig("results/normalized.png")
