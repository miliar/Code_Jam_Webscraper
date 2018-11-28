#include<bits/stdc++.h>

using namespace std;

int main(){
	int t;
	string n, nn;
	scanf("%d", &t);
	for (int c = 1; c <= t; c++) {
		cin >> n;
		nn = n;
		bool prom = true;
		int l = n.size();
		while (prom) {
			prom = false;
			for (int i = 0; i < l - 1; i++) {
				if (n[i] > n[i + 1]) {
					n[i] = n[i] - 1;
					prom = true;
					for (int j = i + 1; j < l; j++) {
						n[j] = '9';
					}
				}
			}		
		}
		printf("Case #%d: ", c);
		//cout << nn << '\n';
		int isp = 0;
		for (int i = 0; i < l; i++) {
			if (n[i] == '0' && isp != 0) {
				cout << n[i];
			} else {
				if (n[i] != '0') {
					isp++;
					cout << n[i];
				}
			}
		}
		printf("\n");
	}	
	return 0;
}
