#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <math.h>

using namespace std;


typedef long long LL;
const double PI = acos(-1);

int main() {
	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		cout << "Case #" << tt + 1 << ": ";
		int n, k;
		cin >> n >> k;
		vector <pair <LL, LL> > a(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i].first >> a[i].second;
		}
		
		sort(a.begin(), a.end(), [](pair <LL, LL> a, pair <LL, LL> b) {
			return a.first * a.second > b.first * b.second;
		});

		LL ans = 0;
		for (int exact = 0; exact < n; exact++) {
			
			LL R = a[exact].first;

			LL cur = 2LL * a[exact].first * a[exact].second;
			
			int cnt = 0;

			for (int i = 0; i < n && cnt < k - 1; i++) {
				if (i == exact) continue;

				cur += 2LL * a[i].first * a[i].second;
				R = max(R, a[i].first); 
				cnt++;
			}
			cur += R * R;
			ans = max(ans, cur);
		}
		cout << fixed << setprecision(10) << PI * (double) ans << "\n";
	
	}
	return 0;
}