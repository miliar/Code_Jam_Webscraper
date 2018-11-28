#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
int n, t, k, p, m, arr[60], ans;
double v1, v2, v3, v4;
vector<int>a[60];
pair<bool,vector<int> > ok(double x) {
	pair<bool, vector<int> >ret;
	for (int i = 1; i <= n; ++i)
		for (int j = 0; j < m; ++j)
			if (a[i][j] >= 0.9 * x * arr[i] && a[i][j] <= 1.1 * x * arr[i]) { 
				ret.second.push_back(j); break; 
			}
	ret.first = (ret.second.size() == n);
	return ret;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	while (p++ < t) {
		cin >> n >> m;
		for (int i = 0; i < 60; ++i)a[i].clear();
		ans = 0;
		for (int i = 1; i <= n; ++i)cin >> arr[i];
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j)cin >> k, a[i].push_back(k);
			sort(a[i].begin(), a[i].end());
		}
		for (int mid = 1; mid <= 1000000;++mid) {
			while (1)
			{
				pair<bool, vector<int> 
				re = ok(mid);
				if (re.first == true) {
					ans ++;
					for (int i = 0; i < n; ++i)a[i+1][re.second[i]] = 0;
				}
				else break;
			}
			
		}
			/*{
			v1 = arr[i];
			for (int j = 1; j <= m; ++j) {
				cin >> v2;
				v3 = v2 / v1;
				y = v3; 
				k = v1 * (double)y * 0.9;
				u = v1 * (double)y * 1.1;
				if (k <= v2 && u >= v2)
					s[y][i]++;
				++y;
				k = v1 * (double)y * 0.9;
				u = v1 * (double)y * 1.1;
				if (k <= v2 && u >= v2)
					s[y][i]++;
				--y,--y;
				k = v1 * (double)y * 0.9;
				u = v1 * (double)y * 1.1;
				if (k <= v2 && u >= v2)
					s[y][i]++;
				
			}
		}
		for (int i = 0; i < 1000100; ++i) {
			k = 1000100;
			for (int j = 1; j <= n; ++j)
				k = min(s[i][j], k);
			ans += k;
		}*/

		cout << "Case #" << p << ": " << ans << endl;
	}
}