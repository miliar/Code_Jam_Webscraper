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

int b, d;
int HD;
map<int,int> res;
map<int,bool> comp;

int _hash(int hd, int ad, int hk, int ak) {
	return (((hd * 101 + ad) * 101 + hk) * 101 + ak);
}

int work(int hd, int ad, int hk, int ak) {
	int h = _hash(hd, ad, hk, ak);
//	cout << h << endl;
	if (res[h]) return res[h];
	if (comp[h]) return 0x7fffffff;
	if (ad >= hk) res[h] = 1;
	else {
		comp[h] = true;
		int ans = 0x7fffffff;
		if (hd > ak) ans = min(ans, work(hd-ak, ad, hk-ad, ak));
		if (hd > ak) ans = min(ans, work(hd-ak, ad+b, hk, ak));
		if (HD > ak) ans = min(ans, work(HD-ak, ad, hk, ak));
		if (hd > ak - d) ans = min(ans, work(hd-max(ak-d,0), ad, hk, max(ak-d,0)));
		if (ans == 0x7fffffff) res[h] = ans;
		else res[h] = ans + 1;
		comp[h] = false;
	}
	return res[h];
}

int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		cout << "Case #" << tt << ": ";
		res.clear();
		comp.clear();
		int hd, ad, hk, ak;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		HD = hd;
		int ans = work(hd, ad, hk, ak);
		if (ans == 0x7fffffff) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}

