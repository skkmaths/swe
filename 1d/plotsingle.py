import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.autolayout'] = True
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 10
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 16
plt.autoscale(enable=True, axis='x', tight=True)
#plt.rcParams['text.usetex'] = True    # This will use Latex fonts (slow)
plt.axis('tight')
plt.autoscale(enable=True, axis='x', tight=True)


u1 = np.loadtxt("solep0.txt") # 



plt.figure()
plt.plot(u1[:,0],u1[:,1],'-',label=r'$\epsilon = 0$',color='black')

#plt.plot(u4[:,0],u4[:,1],'-',label='EPS=$10^{-5}$',color='red')
plt.xlim()
plt.xlabel('x')
plt.ylabel('density')
plt.legend(fontsize=12); plt.grid(True, linestyle = '-', linewidth = 0.5)
#plt.axis('equal')
#plt.yticks(fontsize=12)
plt.savefig('density.pdf')

plt.figure()
plt.plot(u1[:,0],u1[:,2],'-',label=r'$\epsilon = 0$',color='black')

#plt.plot(u4[:,0],u4[:,2],'-',label='EPS=$10^{-5}$',color='red')
plt.xlim()
plt.xlabel('x')
plt.ylabel('velocity')
plt.legend(fontsize=12); plt.grid(True, linestyle = '-', linewidth = 0.5)
#plt.axis('equal')
#plt.yticks(fontsize=12)
plt.savefig('velocity.pdf')

plt.figure()
plt.plot(u1[:,0],u1[:,3],'-',label=r'$\epsilon = 0$',color='black')

#plt.plot(u4[:,0],u4[:,3],'-',label='EPS=$10^{-5}$',color='red')
plt.xlim()
plt.xlabel('x')
plt.ylabel('height')
plt.legend(fontsize=12); plt.grid(True, linestyle = '-', linewidth = 0.5)
#plt.axis('equal')
#plt.yticks(fontsize=12)
plt.savefig('height.pdf')
