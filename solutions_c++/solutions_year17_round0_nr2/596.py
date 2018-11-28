#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAX = 19;
ll pot[MAX];
ll n;
int digits;
ll state = 0, ans;
bool found = false;

void roll(int digit, int last) {
	if(found) {
		return;
	}
	if(digit == 0) {
		found = true;
		ans = state;
		return;
	}
	ford(i, 9, last) {
		state += 1LL * i * pot[digit - 1];	
		if(state <= n) {
			roll(digit - 1, i);
		}
		state -= 1LL * i * pot[digit - 1];
	}
}

int main() {
	ios_base::sync_with_stdio(false);

	pot[0] = 1;
	fori(i, 1, MAX) {
		pot[i] = pot[i - 1] * 10;
	}

	int t;
	cin >> t;
	int kase = 1;
	while(t--) {
		cin >> n;
		digits = to_string(n).size();
		string aux = string(digits, '1');
		if(stoll(aux) > n) {
			digits--;
		}
		found = false;
		state = 0;
		roll(digits, 1);
		cout << "Case #" << kase++ << ": ";
		cout << ans << '\n';
	}

	return 0;
}

