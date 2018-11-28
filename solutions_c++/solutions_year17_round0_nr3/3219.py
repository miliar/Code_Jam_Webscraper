#include <bits/stdc++.h>
using namespace std;
#define int long long
main (){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int z;
	cin >> z;
	for (int cassse = 1; cassse <= z; ++cassse){
		cout << "Case #" << cassse <<": ";
		int kk, n;
		cin >> n >> kk;
		int p = 0;
		int np = 0;
		int m = n;
		if (m&1)np = 1;
		else p = 1;
		kk -= 1;
		while (1){
			if (kk >= np + p){
				int tnp = np;
				int tp = p;
				if(m&1){
					int k = m/2;
					if (k&1){
						np = 2*tnp + tp;  
						p = tp; 
					}
					else{
						np = tp;
						p = 2*tnp + tp;
					}
				}
				else {
					int k = m/2;
					if (k&1){
						np = tp;  
						p = 2*tnp+ tp;
					}
					else{
						np =2*tnp + tp;
						p = tp;
					}
				}
				kk -= tnp;
				kk -= tp;
				m /= 2;
			}
			else {
				if (m&1){
					if(kk+1 <= np){
						cout << m/2 << ' ' << m/2 << '\n';
					}
					else {
						cout << m/2 << ' ' << m/2 - 1 << '\n';
					}
				}
				else {
					if(kk+1 <= p){
						cout << m/2 << ' ' << m/2 - 1 << '\n';
					}
					else {
						cout << m/2 - 1 << ' ' << m/2 - 1 << '\n';
					}
				}
				break;
			}
		}
	}
}
