#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

int Hd, Ad, Hk, Ak, B, D;

int check(int nb, int nd) {
	int hd = Hd; 
	int ad = Ad; 
	int hk = Hk; 
	int ak = Ak;
	for (int day = 1; day <= 1000; ++day) {
		// try to debuff first
		if (nd > 0) {
			if (hd > ak-D) {
				// debuff if no danger
				--nd;
				ak -= D;
				ak = max(ak, 0);
			}
			else {
				hd = Hd; // cure
			}
		}
		else if (nb > 0) {
			if (hd > ak) {
				--nb;
				ad += B;
			}
			else {
				hd = Hd; // cure
			}
		}
		else {
			if (hd > ak || ad >= hk) {
				hk -= ad;
			}
			else {
				hd = Hd; // cure
			}
		}
		if (hk <= 0) return day;
		hd -= ak;
		// cout << day << " " << hd << " " << ad << " " << hk << " " << ak << endl;
		if (hd <= 0) break;
	}
	return 100000000;
}

void solve() {
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	int ans = 100000000;
	for (int Nb = 0; Nb <= 100; ++ Nb)
		for (int Nd = 0; Nd <= 100; ++ Nd) {
			ans = min(ans, check(Nb, Nd));
		}
	if (ans == 100000000) cout << "IMPOSSIBLE";
	else cout << ans;
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int testNum;
	cin >> testNum;
	for (int testid = 0; testid < testNum; ++testid ) {
		cout << "Case #" << testid+1 << ": ";
		solve();
		cout << endl;
	}
}