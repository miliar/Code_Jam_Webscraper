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

const int MAXN = 1111;
int R[MAXN], H[MAXN];

void solve() {
	int N, K;
	cin >> N >> K;
	vector<pii> P(N);
	for (int i = 0; i < N; i++) {
		int R, H;
		cin >> R >> H;
		P[i] = make_pair(R, H);
	}
	sort(P.rbegin(), P.rend());
	const double pi = acos(-1);
	double ans = 0;
	for (int i = 0; i+K <= N; i++) {
		vector<ll> vs;
		for (int j = i+1; j < N; j++) {
			vs.push_back((ll)P[j].first * P[j].second);
		}
		sort(vs.rbegin(), vs.rend());
		double tmp = (ll)P[i].first * P[i].first * pi;
		tmp += (ll)P[i].first * 2 * P[i].second * pi;
		for (int j = 0; j < K-1; j++)
			tmp += 2*vs[j]*pi;
		ans = max(ans, tmp);
	}
	printf("%.10lf\n", ans);
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
