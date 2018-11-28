#include <iostream>
using namespace std;

int main() {
	long t, n;
	cin>>t;
	long c[6],o[6];
	char m[] = "ROYGBV";
	char x[10000];
	long xl;
	for (long ti = 1; ti <= t; ++ti) {
		cout<<"Case #"<<ti<<": ";
		bool yes = true;
		cin>>n;
		for (int i = 0; i < 6; ++i) {
			cin>>o[i];
//			cout<<o[i]<<" ";
		}
		
		for (int j = 0; yes && j < 6; ++j) {
//			cout<<"J"<<j<<"\n";
			for (int i = 0; i < 6; ++i) {
				c[i] = o[i];
			}
			
			int u = 0, l = -1, i = j, tc = 0;
			while(yes && u < n) {
				long ll=l;
				if (c[i]) {
//					cout<<m[i]<<":";
					if ((l == i) ||
						(i == 1 && (l == 0 || i == 2)) ||
						(i == 3 && (l == 2 || i == 4)) ||
						(i == 5 && (l == 4 || i == 0)) ||
						(i == 0 && (l == 1 || i == 5)) ||
						(i == 2 && (l == 1 || i == 3)) ||
						(i == 4 && (l == 3 || i == 5))) {
						if (tc == 6) {
							yes = false;
							break;
						}
						else {
							++tc;
//							cout<<tc<<" ";
							i = (i + 1)%6;
							continue;
						}
					}
					tc = 0;
					x[u] = m[i];
					--c[i];
					++u;
					l = i;
				}
				int mk = 0;
				i = (i + 1)%6;
				mk = i;
				for (int k = 0; k < 6; ++k) {
					if (c[k] > c[mk] && (l != k)) mk = k;
				}
				bool fnd = false;
				for (int k = 0; k < 6; ++k) {
					if (k != mk && c[k]) {
						fnd = true;
						break;
					}
				}
				if (fnd) i=mk;
			}
			if (((x[0] == x[u-1]) ||
				(x[0] == 'O' && (x[u-1] == 'R' || x[u-1] == 'Y')) ||
				(x[0] == 'G' && (x[u-1] == 'Y' || x[u-1] == 'B')) ||
				(x[0] == 'V' && (x[u-1] == 'B' || x[u-1] == 'R')) ||
				(x[0] == 'R' && (x[u-1] == 'O' || x[u-1] == 'V')) ||
				(x[0] == 'Y' && (x[u-1] == 'O' || x[u-1] == 'G')) ||
				(x[0] == 'B' && (x[u-1] == 'G' || x[u-1] == 'V')))
				) {
				yes = false;
			}
			//ROYGBV
			if (!yes && j < 5) {
				yes = true;
				continue;
			}
			else break;
		}
//		cout<<xl<<" ";
		if (yes) {
			x[n] = 0;
			cout<<x;
		}
		else cout<<"IMPOSSIBLE";
		cout<<"\n";
	}
}

