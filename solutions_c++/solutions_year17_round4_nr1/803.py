#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>
#include<cassert>
#include<queue>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
struct cww{cww(){ios::sync_with_stdio(false);cin.tie(0);}}star;

void solve() {
	int N, P;
	cin >> N >> P;
	vector<int> G(N);
	for (int i = 0; i < N; i++) cin >> G[i];
	int ans = 0;
	if (P == 2) {
		int odd = 0;
		for (int i = 0; i < N; i++) {
			odd += G[i]%2;
		}
		ans = N-odd + (odd+1)/2;
	} else if (P == 3) {
		int zero = 0, one = 0;
		for (int i = 0; i < N; i++) {
			if (G[i]%3 == 0) zero += 1;
			else if (G[i]%3==1) one += 1;
		}
		int two = N - zero - one;
		ans = zero;
		int mini = min(one, two);
		ans += mini;
		one -= mini;
		two -= mini;
		ans += (one+2)/3 + (two+2)/3;
	} else {
		vector<int> hoge(4);
		for (int i = 0; i < N; i++) {
			hoge[G[i]%4] += 1;
		}
		ans = hoge[0];
		int mini = min(hoge[1], hoge[3]);
		ans += mini;
		int tmp = max(hoge[1], hoge[3]) - mini;
		ans += (hoge[2]+1) / 2;
		hoge[2] %= 2;
		if (hoge[2] == 0) {
			ans += (tmp+3)/4;
		} else {
			ans += (tmp+1)/4;
		}
	}
	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}
