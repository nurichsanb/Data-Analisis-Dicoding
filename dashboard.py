# -*- coding: utf-8 -*-
"""Dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hmf8EOCLq5nNE1py9HwowUQppy0KMU9N
"""

!pip install streamlit

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive

# Mount dengan Gdrive
drive.mount('/content/drive')

# Membaca dataset
day = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/day.csv",
                          index_col="instant", parse_dates=["dteday"])
hour = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/hour.csv",
                          index_col="instant", parse_dates=["dteday"])

# Menentukan Judul Dashboard
st.title('Dashboard Analisis Data Penyewaan Sepeda')

# Membuat Sidebar
st.sidebar.subheader('Pilih Analisis Data')
analysis_choice = st.sidebar.radio("Pilih Analisis:", ('Tren Jumlah Sepeda per Jam', 'Rata-rata Sepeda Disewakan per Musim',
                                                       'Rata-rata Sepeda Disewakan per Bulan', 'Rata-rata Sepeda Disewakan per Hari dalam Seminggu',
                                                       'Rata-rata Sepeda Disewakan per Hari Libur vs. Hari Kerja'))

# Membuat Analisis Data
if analysis_choice == 'Tren Jumlah Sepeda per Jam':
    st.subheader('Tren Jumlah Sepeda per Jam')
    st.write("Grafik ini menunjukkan tren jumlah sepeda disewakan per jam.")
    st.write("Grafik ini membagi data berdasar musim dan menggambarkan perubahan jumlah sepeda disewakan sepanjang hari.")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=hour, x='hr', y='cnt', hue='season', palette='husl', linewidth=2.5, ax=ax)
    ax.set_title('Tren Jumlah Sepeda Disewakan per Jam', fontsize = 20)
    ax.set_xlabel('Jam (hr)', fontsize = 15)
    ax.set_ylabel('Jumlah Sepeda Disewakan', fontsize = 15)
    ax.legend(title='Musim', loc='upper right', labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    ax.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(fig)

elif analysis_choice == 'Rata-Rata Sepeda Disewakan per Musim':
    st.subheader('Rata-Rata Sepeda Disewakan per Musim')
    st.write("Grafik ini menampilkan rata-rata jumlah sepeda disewakan untuk setiap musim.")
    data_per_musim = day.groupby('season')['cnt'].mean()
    nama_musim = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(nama_musim.values(), data_per_musim.values)
    ax.set_title('Rata-Rata Jumlah Sepeda Disewakan Per Musim', fontsize = 20)
    ax.set_xlabel('Musim', fontsize = 15)
    ax.set_ylabel('Rata-Rata Jumlah Sepeda Disewakan', fontsize = 15)
    ax.set_xticklabels(nama_musim.values(), rotation=15, ha='right')
    st.pyplot(fig)

elif analysis_choice == 'Rata-Rata Sepeda Disewakan per Bulan':
    st.subheader('Rata-Rata Sepeda Disewakan per Bulan')
    st.write("Grafik ini menunjukkan rata-rata jumlah sepeda disewakan per bulan.")
    data_per_bulan = day.groupby('mnth')['cnt'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_per_bulan.index, data_per_bulan.values, marker='o', linestyle='-')
    ax.set_title('Jumlah Sepeda Disewakan Per Bulan', fontsize = 20)
    ax.set_xlabel('Bulan', fontsize = 15)
    ax.set_ylabel('Jumlah Sepeda Disewakan', fontsize = 15)
    ax.grid(True)
    ax.set_xticks(data_per_bulan.index)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
    st.pyplot(fig)

elif analysis_choice == 'Rata-Rata Sepeda Disewakan per Hari dalam Seminggu':
    st.subheader('Rata-Rata Sepeda Disewakan per Hari dalam Seminggu')
    st.write("Grafik ini menampilkan rata-rata jumlah sepeda disewakan per hari dalam seminggu.")
    data_per_hari = day.groupby('weekday')['cnt'].mean()
    nama_hari = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(nama_hari, data_per_hari.values)
    ax.set_title('Rata-Rata Jumlah Sepeda Disewakan per Hari dalam Seminggu', fontszie = 20)
    ax.set_xlabel('Hari dalam Seminggu', fontsize = 15)
    ax.set_ylabel('Rata-rata Jumlah Sepeda Disewakan', fontsize = 15)
    ax.set_xticklabels(nama_hari, rotation=45)
    st.pyplot(fig)

elif analysis_choice == 'Rata-Rata Sepeda Disewakan per Hari Libur vs. Hari Kerja':
    st.subheader('Rata-Rata Sepeda Disewakan per Hari Libur vs. Hari Kerja')
    st.write("Grafik ini menampilkan rata-rata jumlah sepeda disewakan per hari libur dan hari kerja.")
    data_hari_libur = day[day['holiday'] == 1]['cnt'].mean()
    data_hari_kerja = day[day['workingday'] == 1]['cnt'].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(['Hari Libur', 'Hari Kerja'], [data_hari_libur, data_hari_kerja])
    ax.set_title('Rata-rata Jumlah Sepeda Disewakan per Hari Libur vs. Hari Kerja', fontsize = 20)
    ax.set_xlabel('Jenis Hari', fontsize = 15)
    ax.set_ylabel('Rata-rata Jumlah Sepeda Disewakan', fontsize = 15)
    st.pyplot(fig)

# Membuat bagian keterangan
st.sidebar.subheader('Kesimpulan dan Implikasi')
st.sidebar.write("**Kesimpulan Pertanyaan 1:** Bagaimana tren penyewaan dan apa saja faktor yang berpengaruh pada perubahan tren sepanjang tahun?")
st.sidebar.write("Dari analisis data yang telah dilakukan, dapat disimpulkan bahwa:")
st.sidebar.write("- Pola atau tren penyewaan sepeda menunjukan perubahan yang signifikan, tren menunjukan peningkatan dari musim semi hingga musim gugur puncak penyewaan tertinggi, dan mulai mengalami penurunan pada musim dingin.")
st.sidebar.write("- Pada hari kerja, penyewaan sepeda cenderung menunjukan jumlah yang lebih tinggi daripada hari libur.")
st.sidebar.write("- Cuaca, musim, dan suhu merupakan faktor kuat yang sangat mempengaruhi tren penyewaan sepeda.")

st.sidebar.write("**Kesimpulan Pertanyaan 2:** Bagaimana pola musiman penyewaan sepeda membantu decision-making persedian sepeda?")
st.sidebar.write("Pola Harian")
st.sidebar.write("- Musim Semi: Rata-Rata Jumlah Sepeda Disewakan = 2604.13")
st.sidebar.write("- Musim Panas: Rata-Rata Jumlah Sepeda Disewakan = 4992.33")
st.sidebar.write("- Musim Gugur: Rata-Rata Jumlah Sepeda Disewakan = 5644.3")
st.sidebar.write("- Musim Dingin: Rata-Rata Jumlah Sepeda Disewakan = 4728.16")

st.sidebar.write("Pola Mingguan")
st.sidebar.write("- Hari Kerja (Weekday): Rata-Rata Jumlah Sepeda Disewakan = 4584.82")
st.sidebar.write("- Hari Libur (Weekend): Rata-Rata Jumlah Sepeda Disewakan = 3735.0")

st.sidebar.write("**Implikasi:**")
st.sidebar.write("Pada hari kerja, peminjaman sepeda lebih banyak terjadi dibandingkan dengan hari libur. Fakta ini menunjukkan peluang bisnis potensial pada hari-hari kerja, dan perusahaan sebaiknya mempertimbangkan strategi pemasaran dan promosi khusus untuk menarik pelanggan selama periode tersebut.")
st.sidebar.write("Selama musim panas dan musim gugur, tingkat permintaan sepeda mencapai puncaknya. Oleh karena itu, diperlukan peningkatan strategi persediaan sepeda untuk memastikan ketersediaan yang memadai selama periode dengan permintaan tinggi ini.")
st.sidebar.write("Analisis pola musiman memberikan wawasan berharga dalam perencanaan persediaan sepeda, memungkinkan perusahaan untuk mengoptimalkan manajemen inventaris mereka. Pendekatan ini dapat mencegah ketidakseimbangan antara permintaan dan persediaan, yang pada gilirannya dapat meningkatkan kepuasan pelanggan dan efisiensi operasional.")