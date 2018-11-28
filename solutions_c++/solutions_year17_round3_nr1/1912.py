#include <bits/stdc++.h>
using namespace std;

typedef long double ld;
typedef pair <long double, long double> pld;

ld PI = atan(1) * 4;

int n, k;

int main() {
	ios_base::sync_with_stdio (false), cin.tie (NULL);
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; ++cas) {
	    cin >> n >> k;
	    vector <pld> cakes;
	    for (int i = 0; i < n; ++i) {
	        ld r, h;
	        cin >> r >> h;
	        cakes.push_back ({r, h});
	    }
	    sort (cakes.begin(), cakes.end());
	    priority_queue <ld> pq;
	    ld ans = 0;
	    for (int i = 0; i < n; ++i) {
	        ld s = PI * cakes[i].first * cakes[i].first + 2 * PI * cakes[i].first * cakes[i].second;
	        if (i < k - 1) {
	            pq.push (2 * PI * cakes[i].first * cakes[i].second);
	            continue;
	        }
	        vector <ld> v;
	        for (int j = 0; j < k - 1; ++j) {
	            s += pq.top();
	            v.push_back (pq.top());
	            pq.pop();
	        }
	        for (int j = 0; j < k - 1; ++j)
	            pq.push (v[j]);
	        pq.push (2 * PI * cakes[i].first * cakes[i].second);
	        ans = max (ans, s);
	    }
	    cout << "Case #" << cas << ": " << fixed << setprecision(9) << ans << '\n';
	}
	return 0;
}
