#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int, int> pii;

int T;
int n;

void load() {
	cin >> n;
}

bool tidy(int n) {
	int lst = 10;
	do {
		int cur = n % 10;
		if (cur > lst) return false;
		lst = cur;
	} while (n /= 10);
	return true;
}

void solve(int tc) {
	cout << "Case #" << tc << ": ";
	while (n > 0) {
		if (tidy(n)) break;
		--n;
	}
	cout << n << endl;
}

void clear() {
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		clog << tc << "/" << T << endl;
		load();
		solve(tc);
		clear();
	}
	return 0;
}
