#include<bits/stdc++.h>
using namespace std;

const double INF = 1e13;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for(int I = 1; I <= T; ++I){
		cout << "Case #" << I  << ": ";
		int N,Q;
		cin >> N >> Q;
		vector<double> d(N);
		vector<double> s(N);
		for(int i = 0; i < N; ++i){
			cin >> d[i] >> s[i];
		}
		vector<vector<double> > dp(N, vector<double> (N,INF));
		for(int i = 0; i < N; ++i){
			for(int j = 0; j < N; ++j){
				int x;
				cin >> x;
				if(x != -1) dp[i][j] = x;
			}
		}
		/*
		for(int i = 0; i < N; ++i){
 			dp[i][i] = 0;
		}
		*/
		for(int k = 0; k < N; ++k){
			for(int i = 0; i < N; ++i){
				for(int j = 0; j < N; ++j){
					dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
				}
			}
		}
		//vector<vector<long long> > t = dp;
		for(int i = 0; i < N; ++i){
			for(int j = 0; j < N; ++j){
				if(dp[i][j] <= d[i]) dp[i][j] /= s[i];
				else dp[i][j] = INF;
			}
		}

		for(int k = 0; k < N; ++k){
			for(int i = 0; i < N; ++i){
				for(int j = 0; j < N; ++j){
					dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
				}
			}
		}

		while(Q--){
			int x,y;
			cin >> x >> y;
			cout.setf(ios::fixed);
			cout.precision(10);
			cout << dp[--x][--y] <<' ';
		}
		cout << endl;
	}
}
