#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int e[111], s[111], d[111], dt[111];
int N, Q; 
double dp[111][111];
double f(int at, int hno) {
	if(at == N - 1) {
		return 0.0;
	}
	if(dp[at][hno] > -1) return dp[at][hno];

	double t1 = (d[at + 1] * 1.0 / s[at] ) + f(at + 1, at);
	double t2 = (d[at + 1] * 1.0 / s[hno]) + f(at + 1, hno);

	double ans = 0.0;
	if(e[hno] >= dt[at + 1] - dt[hno]){
		ans = min(t2, t1);
	}else ans = t1;

	return dp[at][hno] = ans;

}

int main() {

	int T; cin >> T;
	for(int tc = 1; tc <= T; tc ++){
		
		for(int i = 0; i < 111; i++) for(int j = 0; j < 111; j++) dp[i][j] = -1;
		
		cin >> N >> Q;
		
		for(int i = 0; i < N; i++) cin >> e[i] >> s[i];

		d[0] = 0;
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				int x; cin >> x;
				if(j == i+1) {
					d[j] = x;
				}
			}
		}
		int u, v; cin >> u >> v;
		dt[0] = 0;
		for(int i = 1; i < N; i++){
			dt[i] = dt[i-1] + d[i];
		}

		double ans = f(0, 0);
		printf("Case #%d: %.7f\n", tc, ans);
		//cout << "Case #" << tc << ": " << ans << endl;


	}

	return 0;
}