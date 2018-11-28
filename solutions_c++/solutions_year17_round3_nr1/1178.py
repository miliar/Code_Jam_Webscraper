#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>

using namespace std;

#define REP(a, b, c) for(int a=(b); a<(c); a++)
#define dREP(a, b, c) for(int a=(b); a>=(c); a--)
#define pR first
#define pH second

int T, N, K;

vector< pair<int, int> > p(1010);

long long dp[1010], mx[1010];

double PI = 3.14159265358979323846;

int main(){
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> N >> K;
		p.clear();
		p.resize(N);
		REP(i, 0, N){
			cin >> p[i].pR >> p[i].pH;
		}
		sort(p.begin(), p.end());
		REP(i, 0, N){
			dp[i] = ((long long)p[i].pR)*2*p[i].pH;
			if(i) mx[i] = max(mx[i-1], dp[i]);
			else mx[i] = dp[i];
		}
		REP(k, 1, K){
			REP(i, k, N){
				dp[i] = mx[i-1]+((long long)p[i].pR)*2*p[i].pH;
			}
			REP(i, k, N){
				if(i>k) mx[i] = max(mx[i-1], dp[i]);
				else mx[i] = dp[i];
			}
		}
		long long ansll = dp[K-1]+(((long long)p[K-1].pR)*p[K-1].pR);
		REP(i, K-1, N){
			ansll = max(ansll, dp[i]+(((long long)p[i].pR)*p[i].pR));
		}
		printf("Case #%d: %.9f\n", t, PI*ansll);
	}
	return 0;
}
