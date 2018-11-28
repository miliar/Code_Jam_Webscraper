#include <bits/stdc++.h>
#define ll long long
#define to_str(x) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

using namespace std;
int t, k, cases;

bool isTidy(ll x) {
	set<vector<int> > st;
	vector<int> vec;
	while (x) {
		vec.push_back(x % 10);
		x /= 10;
	}
	reverse(vec.begin(), vec.end());
	st.insert(vec);
	sort(vec.begin(), vec.end());
	st.insert(vec);
	return (st.size() == 1);
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> t;
	while (t--) {
		cin >> k;
		int ans = 0;
		for (int i = k; i > 0; --i) {
			if (isTidy(i)) {
				ans = i;
				break;
			}
		}
		cout << "Case #" << ++cases << ": " << ans << endl;
	}
	return 0;
}
