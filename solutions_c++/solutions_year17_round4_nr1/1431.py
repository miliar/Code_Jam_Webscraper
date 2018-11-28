#include <bits/stdc++.h>
using namespace std;

const int MAX_V = 100;
const int MAX_P = 4;
int T, N, P;
long long g[MAX_P];

void get(long long x){
	for(int i=0; i<P; ++i){
		g[i] = x % MAX_V;
		x /= MAX_V;
	}
}

long long put(){
	long long x = 0;
	for(int i=P-1; i>=0; --i){
		x *= MAX_V;
		x += g[i];
	}
	return x;
}

long long dp[MAX_P][MAX_V*MAX_V*MAX_V*MAX_V];

int main(){
	if(fopen("test.in","r")){
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t){
		memset(dp, 0, sizeof(dp));
		memset(g, 0, sizeof(g));
		cin >> N >> P;
		for(int i=0; i<N; ++i){
			int x;
			cin >> x;
			++g[x%P];
		}
		long long x = put();
		dp[0][x] = 1;
		for(int i=x; i>=0; --i){
			for (int p=0; p<P; ++p){
				long long num = dp[p][i];
				if(num){
					if(p == 0) ++num;
					get(i);
					for(int j=0; j<P; ++j) if(g[j]){
						--g[j];
						// if(num) cout << i << " " << p << " " << j << " " << num << endl;
						long long next_x = put();
						long long next_p = (P + p - j) % P;
						dp[next_p][next_x] = max(dp[next_p][next_x], num);
						++g[j];
					}
				}
			}
		}
		long long best = 0;
		for(int i=0; i< P; ++i) best = max(best, dp[i][0]-1);
		cout << "Case #" << t << ": " << best << endl;
	}
}
