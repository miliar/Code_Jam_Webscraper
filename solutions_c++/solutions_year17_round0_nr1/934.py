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
	string S;
	int K;
	cin >> S >> K;
	int N = S.size();
	vector<int> vs(N);
	for (int i = 0; i < N; i++)
		vs[i] = (S[i] == '+' ? 1 : 0);	
	int ans = 0;
	for (int i = 0; i <= N-K; i++) {
		if (!vs[i]) {
			for (int j = 0; j < K; j++) {
				vs[i+j] ^= 1;
			}
			++ans;
		}
	}
	for (int i = 0; i < N; i++) {
		if (!vs[i]) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}
