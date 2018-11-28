#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int ile[5];
int tab[10007];
int kol[4];

int licz(int n) {
	int sum = 0;
	int wyn = 0;
	for(int i = 1; i <= n; ++i) {
		if(sum % 4 == 0) wyn++;
		sum += tab[i];
	}
	return wyn;
}

int main() {
	ios_base::sync_with_stdio(0);
	int tt;
	cin >> tt;
	for(int it = 1; it <= tt; ++it) {
		int n, p;
		cin >> n >> p;
		for(int i = 0; i < 5; ++i) ile[i] = 0;
		for(int i = 1; i <= n; ++i) {
			int x;
			cin >> x;
			ile[x % p]++;
		}
		
		cout << "Case #" << it << ": ";
		
		if(p == 2) {
			int res = (ile[1] + 1) / 2;
			res += ile[0];
			cout << res << '\n';
		}
		else if(p == 3) {
			int res = min(ile[1], ile[2]);
			if(ile[1] > ile[2]) {
				ile[1] -= res;
				res += (ile[1] + 2) / 3;
			}
			else {
				ile[2] -= res;
				res += (ile[2] + 2) / 3;
			}
			res += ile[0];
			cout << res << '\n';
		}
		else {
			int res = min(ile[1], ile[3]);
			ile[1] -= res;
			ile[3] -= res;
	
			res += ile[0];
	
			kol[1] = 1;
			kol[2] = 2;
			kol[3] = 3;
	
			int res2 = 0;
	
			do {
				int lc = 1;
				for(int i = 0; i < ile[kol[1]]; ++i, ++lc) tab[lc] = kol[1];
				for(int i = 0; i < ile[kol[2]]; ++i, ++lc) tab[lc] = kol[2];
				for(int i = 0; i < ile[kol[3]]; ++i, ++lc) tab[lc] = kol[3];
				res2 = max(res2, licz(lc - 1));
			}while(next_permutation(kol + 1, kol + 4));
			res += res2;
			cout << res << '\n';
		}
	}
	return 0;
}
