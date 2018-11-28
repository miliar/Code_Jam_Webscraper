#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define vec vector
#define INF 1000000007
#define pii pair<int, int>
#define mp make_pair

pii find(int q, int r)
{
	int right = (int)((double)q * 10.0 / 9.0 / (double)r);
	int left = right;
	while(r * (left - 1) * 11 >= q * 10) left--;
	if (r * left * 11 < q * 10) left++;
	return mp(left, right);
}

int main(void)
{
	// cout << find(450, 50).first << " " << find(450, 50).second << endl;
	// cout << find(449, 50).first << " " << find(449, 50).second << endl;
	// cout << find(1101, 100).first << " " << find(1101, 100).second << endl;
	// cout << find(1100, 100).first << " " << find(1100, 100).second << endl;
	int T;
	cin >> T;
	rep(t, T) {
		cout << "Case #" << t + 1 << ": ";

		int n, p;
		cin >> n >> p;
		vec<int> r(n);
		vec<vec<pii>> q(n, vec<pii>(p));
		rep(i, n) cin >> r[i];
		rep(i, n) {
			vec<int> temp(p);
			rep(j, p) cin >> temp[j];
			sort(temp.begin(), temp.end());
			rep(j, p) q[i][j] = find(temp[j], r[i]);
		}

		vec<int> cur(n, 0);
		int ans = 0;
		while(cur[0] < p) {
			int flag = 1;
			int num = q[0][cur[0]].first;
			if(num > q[0][cur[0]].second) {
				cur[0]++;
				continue;
			}
			while(num <= q[0][cur[0]].second) {
				flag = 1;
				rep(i, n - 1) {
					while(cur[i + 1] < p && q[i + 1][cur[i + 1]].second < num) {
						cur[i + 1]++;
					}
					if (cur[i + 1] == p || q[i + 1][cur[i + 1]].first > num) {
						flag = 0;
						break;
					}
				}
				if (flag) break;
				num++;
			}
			cur[0]++;
			if (flag) {
				ans++;
				rep(i, n - 1) cur[i + 1]++;
			}
		}
		cout << ans << endl;
	}
	return 0;
}
