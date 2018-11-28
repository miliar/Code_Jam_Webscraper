#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;

#define pb push_back

using namespace std;

int T;
int cnt[4];
int n;
int p;

void load () {
	fill (cnt, cnt + 4, 0);
	cin >> n >> p;
	clog << n << endl;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		cnt[a % p]++;
	}
}

void solve (int tc) {
	int ans = 0;
	if (p == 2) {
		ans = cnt[1] / 2;
	}
	else if (p == 3) {
		ans = 0;
		int v = min (cnt[1], cnt[2]);
		cnt[1] -= v;
		cnt[2] -= v;
		ans = v;
		v = max (cnt[1], cnt[2]);
		ans += v - (v + 2) / 3;
	}
	else {
		clog << cnt[1] << ' ' << cnt[2] << ' ' << cnt[3] << endl;
		int v = min (cnt[1], cnt[3]);
		cnt[1] -= v;
		cnt[3] -= v;
   		clog << v << endl;
		ans = v;
		v = cnt[2] >> 1;
		cnt[2] -= 2 * v;
		ans += v;
		while (cnt[1] >= 2 && cnt[2]) {
			cnt[1] -= 2;
			cnt[2] --;
			ans += 2;
		}
		while (cnt[3] >= 4) {
			ans += 3;
			cnt[3] -= 4;
		}
		while (cnt[1] >= 4) {
			cnt[1] -= 4;
			ans += 3;
		}
		vector<int> pp;
		for (int i = 1; i <= 3; i++) {
			for (int j = 0; j < cnt[i]; j++) {
				pp.pb (i);
			}
		}
		int AD = 1e9;
		if (pp.empty ())
			AD = 0;
		do {
			int add = 0;
			int ost = 0;
			for (auto to : pp) {
				if (ost)
					add++;
				ost = (ost + to) % p;
			}
			AD = min (AD, add);
		} while (next_permutation (pp.begin (), pp.end ()));
		ans += AD;
	}
	cout << "Case #" << tc << ": " << n - ans << endl;
}

void clear () {
}

int main () {
#ifdef LOCAL
    freopen ("file.in", "r", stdin);
    freopen ("file.out", "w", stdout);
#endif 
	
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		load ();
		solve (tc);
		clear ();
	}

    return 0;
}