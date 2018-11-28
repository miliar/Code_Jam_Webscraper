#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pll pair<ll, ll>
#define F first
#define S second
#define mp make_pair
#define pb push_back

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		double N, D;
		cin >> D >> N;
		double ans = 1e16;
		double S, K;
		for(int i = 0; i < N; i++){
			cin >> K >> S;
			double res = (K * S + S*(D - K))/(D - K);
			ans  = min(ans, res);
		}
		printf("Case #%d: %.8lf\n", t, ans);
	}
	return 0;
}