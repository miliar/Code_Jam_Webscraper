#include<bits/stdc++.h>
using namespace std;
pair<int, int> test(int n, int k) {
	vector<bool> a(n + 2, 0);
	a[0] = true;
	a[n + 1] = true;
	int pre = 0;
	int mi = n + 10;
	int ma;
	int dd = -1, le, ri, ix, prex;
	int kk = 1;
	while (kk <= k) {
		//cerr<<kk<<endl;
		mi = 0;
		ma = 0;
		pre = 0;
		for (int i = 1; i <= n + 1; ++i) {
			if (a[i]) {
				int t = (i + pre) / 2;
				if (kk == 490) {
					//		cerr << pre<<" "<<i <<" "<<t<< endl;
				}
				if (a[t]) {
					pre = i;
					continue;
				}
				//	cout << t << " " << pre << " " << i << endl;
				le = t - pre - 1;
				ri = i - t - 1;
				if (min(le, ri) > mi) {
					mi = min(le, ri);
					ma = max(le, ri);
					dd = t;
					ix = i;
					prex = pre;
				} else if ((min(le, ri) == mi) && (max(le, ri) > ma)) {
					mi = min(le, ri);
					ma = max(le, ri);
					dd = t;
					ix = i;
					prex = pre;
				}
				/*if (kk == 490) {
				 cerr << t << " " << pre << " " << i << " " << le << " "
				 << ri << " " << mi << " " << ma << endl;
				 }*/
				//	cout << t << " " << le << " " << ri << endl;
				pre = i;
			}
			//		cerr<<i<<" "<<mi<<" "<<ma<<endl;
		}
		if (dd != -1) {
			if (a[dd]) {
				//		cerr<<dd<<endl;
			}
			a[dd] = 1;
			//		cerr << kk << " " << dd << " " << mi << " " << ma << endl;
		}
		kk++;
	}
//	cerr << ma << " " << mi << endl;
	return {ma,mi};
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t;
	cin >> t;
	long long n, k;
	for (int i = 1; i <= t; ++i) {
	//	cerr << i << endl;
		long long tot = 0;
		cin >> n >> k;
		/*if (n > 290000) {
		 if (n < 400000)
		 cerr << n << " " << k << endl;
		 continue;
		 }*/
		/*pair<int, int> ans2 = test(n, k);
		 cout << "Case #" << i << ": ";
		 cout << ans2.first << " " << ans2.second << endl;*/
		 cout << "Case #" << i << ": ";
		long long a[2][2];
		long long ans[2];
		memset(a, 0, sizeof a);
		a[n % 2][0] = n;
		a[n % 2][1] = 1;
		bool st;
		while (1) {
			/*for (int i = 0; i < 2; ++i) {
				for (int j = 0; j < 2; ++j) {
					cerr << a[i][j] << " ";
				}
				cerr << endl;
			}
			cerr << endl;*/
			if (a[0][0] > a[1][0]) {
				st = 0;
			} else {
				st = 1;
			}
			tot += a[st][1];
		//	cerr << "tot= " << tot << " " << k << endl;
			if (tot >= k) {
				a[st][0]--;
				bool xx = a[st][0] % 2;
				//cout << a[st][0] / 2 + xx << " " << a[st][0] / 2 << endl;
				ans[0] = a[st][0] / 2 + xx;
				ans[1] = a[st][0] / 2;
				break;
			}
			tot += a[!st][1];
	//		cerr << "tot= " << tot << " " << k << endl;
			if (tot >= k) {
				a[!st][0]--;
				bool xx = a[!st][0] % 2;
				//cout << a[!st][0] / 2 + 1 << " " << a[!st][0] / 2 << endl;
				ans[0] = a[!st][0] / 2 + xx;
				ans[1] = a[!st][0] / 2;
				break;
			}
			if (a[0][0] == 0) {
				a[1][0]--;
				long long ff = a[1][0] / 2;
				bool xx = ff % 2;
				a[xx][0] = ff;
				a[xx][1] = a[1][1] * 2;
				a[!xx][0] = 0;
				a[!xx][1] = 0;
			} else if (a[1][0] == 0) {
				a[0][0]--;
				long long ff = a[0][0] / 2;
				bool xx = ff % 2;
				a[xx][0] = ff;
				a[!xx][0] = ff + 1;
				a[xx][1] = a[0][1];
				a[!xx][1] = a[0][1];
			} else {
				int c[2][2];
				memset(c, 0, sizeof c);
				a[1][0]--;
				long long ff = a[1][0] / 2;
				bool xx = ff % 2;
				c[xx][0] = ff;
				c[xx][1] = a[1][1] * 2;

				a[0][0]--;
				ff = a[0][0] / 2;
				xx = ff % 2;
				c[xx][0] = ff;
				c[!xx][0] = ff + 1;
				c[0][1] += a[0][1];
				c[1][1] += a[0][1];
				a[0][0] = c[0][0];
				a[0][1] = c[0][1];
				a[1][0] = c[1][0];
				a[1][1] = c[1][1];
			}
		}
		cout << ans[0] << " " << ans[1] << endl;
		/*if (ans[0] != ans2.first && ans[1] != ans2.second) {
		 cerr << i << endl;
		 cerr << n << " " << k << endl;
		 }*/
	}
	return 0;

}
