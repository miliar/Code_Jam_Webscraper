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
	int N, C, M;
	cin >> N >> C >> M;
	vector<int> P(M), B(M);
	for (int i = 0; i < M; i++) {
		cin >> P[i] >> B[i];
		--P[i]; --B[i];
	}
	vector<int> cnt(C), degree(N);
	for (int i = 0; i < M; i++) {
		cnt[B[i]]++;
		degree[P[i]]++;
	}
	int ans = *max_element(cnt.begin(), cnt.end());
	int sum = 0;
	for (int i = 0; i < N; i++) {
		sum += degree[i];
		ans = max(ans, (degree[i]+i) / (i+1));
	}
	int num = 0;
	for (int i = 0; i < N; i++) {
		num += max(0, degree[i]-ans);
	}
	cout << ans << " " << num << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": " ;
		solve();
	}
	return 0;
}
