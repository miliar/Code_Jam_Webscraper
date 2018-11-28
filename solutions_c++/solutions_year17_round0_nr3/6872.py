#include <bits/stdc++.h>
using namespace std;

int ls(int i, bool pres[]) {
	int k = 0;
	for(int j = i - 1; j >= 0; j--) {
		if (!pres[j]) {
			k++;
		}
		else {
			break;
		}
	}
	return k;
}
int rs(int i, bool pres[]) {
	int k = 0;
	for(int j = i + 1; ; j++) {
		if (!pres[j]) {
			k++;
		}
		else {
			break;
		}
	}
	return k;
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n ; i++) {
		int tam, p;
		cin >> tam >> p;
		bool pres[tam + 2];
		for (int j = 1; j <= tam; j++) {
			pres[j] = false;
		}
		pres[0] = true;
		pres[tam + 1] = true;
		int k = 0;
		while(p > 0) {
			k = 0;
			int space = -1;
			for (int j = 1; j <= tam; j++) {
				if (!pres[j]) {
					int a = min(ls(j,pres),rs(j, pres));
					if (a > space) {
						space = a;
						k = j;
					}
					else if (a == space) {
						if (max(ls(j,pres),rs(j, pres)) > max(ls(k,pres),rs(k, pres))) {
							k = j;
						}
					}
				}
			}
			pres[k] = true;
			p--;
		}
		cout << "Case #" << i + 1 << ": " << max(ls(k,pres),rs(k, pres)) << " " << min(ls(k,pres),rs(k, pres)) << endl;
	}
}
