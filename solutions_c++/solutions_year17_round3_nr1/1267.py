#include<bits/stdc++.h>
#define int long long
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define INF (1ll<<60)
typedef pair<int, int> pii;
#define R first
#define H second
#define S first
#define I second

int N, K;
pii cakes[1010];
pii yoko[1010];

int calc(int la) {
	int k = 0;
	int res = 0;
	for (int i = 0; k < K-1; ++i) {
		if (yoko[i].I>la) {
			res += yoko[i].S;
			k++;
		}
	}
	return res;
}

int solve() {
	cin >> N >> K;
	rep(i, N) {
		cin >> cakes[i].R >> cakes[i].H;
	}
	sort(cakes, cakes + N, greater<pii>());
	rep(i, N) {
		yoko[i] = pii(cakes[i].R * cakes[i].H * 2, i);//*PI
	}
	sort(yoko, yoko + N, greater<pii>());
	int ma = -INF;
	rep(i, N - K+1) {
		ma = max(ma, calc(i) + cakes[i].R*cakes[i].R + cakes[i].R * cakes[i].H * 2);
	}
	return ma;
}

signed main() {
	int t;
	cin >> t;
	cout << setprecision(15);
	rep(i, t) {
		int ans = solve();
		memset(cakes, 0, sizeof(cakes));
		memset(yoko, 0, sizeof(yoko));
		cout << "Case #" << i + 1 << ": " << 1.*ans*3.141592653589793238 << endl;
	}
}
