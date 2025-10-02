import matplotlib.pyplot as plt

# 频率（Hz）
freq = [7e3, 1e5, 1e6, 2.5e6, 4e6, 5e6, 1e7, 1.5e7, 2e7]
# 各种接地配置下的干扰电压（mV）
no_copper = [12, 12, 11, 21, 30, 38, 70, 120, 125]
large_copper = [12, 12, 7, 10, 14, 18, 30, 50, 60]
small_copper_mid = [None, None, 6, 8, 10, 13, 22, 40, 40]
small_copper_edge = [None, None, 10, None, None, 31, 64, None, 125]

plt.figure(figsize=(8,5))
plt.plot(freq, no_copper, 'o-', label='No copper plate')
plt.plot(freq, large_copper, 's-', label='Large copper plate')
plt.plot(freq, small_copper_mid, '^-', label='Small copper plate (center bridge)')
plt.plot(freq, small_copper_edge, 'd-', label='Small copper plate (edge bridge)')
plt.xscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Interference voltage (mV)')
plt.title('Crosstalk vs Frequency for Different Ground Plane Configurations')
plt.legend()
plt.grid(True, which='both')
plt.tight_layout()
plt.savefig('output_B.png')  # 保存为图片
# plt.show()  # 可选，显示图像
