import matplotlib.pyplot as plt

# 数据
freq = [7e3, 1e5, 1e6, 5e6, 1e7, 1.5e7, 2e7]
K_none = [0.28, 0.30, 1.39, 6.85, 10.00, 15.28, 19.44]
K_single = [0.35, 0.30, 1.33, 6.79, 8.89, 14.72, 18.33]
K_double = [0.35, 0.20, 0.33, 1.23, 2.50, 3.33, 4.11]

plt.figure(figsize=(8,5))
plt.plot(freq, K_none, 'o-', label='no ground')
plt.plot(freq, K_single, 's-', label='single-ended ground')
plt.plot(freq, K_double, '^-', label='double-ended ground')
plt.xscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized Coupling Coefficient K (%)')
plt.title('Coupling Coefficient vs Frequency for Different Grounding Methods')
plt.legend()
plt.grid(True, which='both')
plt.tight_layout()
plt.savefig('output.png')  # 保存为图片
# plt.show()  # 可选，显示图像
