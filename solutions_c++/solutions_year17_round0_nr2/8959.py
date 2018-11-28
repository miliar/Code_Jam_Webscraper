#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

bool good(int x) {
	string sx = to_string(x);
	char last = '0';
	fori(i, 0, sx.size()) {
		if(sx[i] < last) {
			return false;
		}
		last = sx[i];
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);

	int casos;
	cin >> casos;
	fori(caso, 1, casos + 1) {
		int n;
		cin >> n;
		int ans = -1;
		fori(i, 1, n + 1) {
			if(good(i)) {
				ans = i;
			}
		}
		cout << "Case #" << caso << ": " << ans << '\n';
	}

	return 0;
}

