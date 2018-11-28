#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <map>

using namespace std;



int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		cout << "Case #" << tt << ": ";
		int n, p;
		cin >> n >> p;
		int g[100];
		for (int i = 0; i < n; i ++) {
			cin >> g[i];
		}
		if (p == 2) {
			int a[2] = {0,0};
			for (int i = 0; i < n; i ++) a[g[i]%2] ++;
			cout << a[0] + a[1]/2 + a[1]%2 << endl;
		} else if (p == 3) {
			int a[3] = {0,0,0};
			for (int i = 0; i < n; i ++) a[g[i]%3] ++;
			int maxbc = max(a[1],a[2]), minbc = min(a[1],a[2]);
			cout << a[0] + minbc + (maxbc - minbc) / 3 + ((maxbc-minbc)%3?1:0)<< endl;
		} else if (p == 4) {
			int a[4] = {0,0,0,0};
			for (int i = 0; i < n; i ++) a[g[i]%4] ++;
			int ans = a[0];
			int temp = min(a[1],a[3]); ans += temp; a[1]-=temp; a[3] -= temp;
			ans += a[2]/2; a[2]%=2;
			if (a[2]==1 && a[1]>=2) { ans++; a[2]--; a[1]-=2; }
			if (a[2]==1 && a[3]>=2) { ans++; a[2]--; a[3]-=2; }
			ans += a[1]/4; a[1]%=4;
			ans += a[3]/4; a[3]%=4;
			if (a[1] || a[2] || a[3]) ans ++;
			cout << ans <<endl;
		}
	}
	return 0;
}

