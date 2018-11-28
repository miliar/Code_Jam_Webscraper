#include <bits/stdc++.h>

using namespace std; 

typedef pair<int, int> pii;
typedef long long ll;
#define mp make_pair
#define pb push_back

string solve () {
	string n, tmp, ans;
	cin >> n;
	
	tmp = n; 

	ans = tmp;
	int l = 0;
	bool flag = false;
	for (int i = 1; i < (int) tmp.size(); i++) {
		if (tmp[i] >= tmp[i - 1]) {
			ans[i] = tmp[i];
		} else {
			break;
		}
		if (tmp[i - 1] != tmp[i])
			l = i;
		flag = (i == (int) tmp.size() - 1);
	}
	if (!flag && (int) ans.size() > 1) {
		ans[l] --;
		for (int i = l + 1; i < (int) tmp.size(); i++) {
			ans[i] = '9';
		}
	}

	l = 0;
	for (; l < (int) ans.size() && ans[l] == '0'; l++);
	return ans.substr(l);
}
int main () {
#ifdef LOCAL
	freopen ("test.in", "r", stdin);
	freopen ("test.out", "w", stdout);
#endif

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": " << solve() << "\n";
	}
	return 0;
}