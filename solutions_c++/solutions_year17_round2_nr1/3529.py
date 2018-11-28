#include<iostream>
#include<algorithm>

using namespace std;

#define REP(a, b, c) for(int a=(b); a<(c); a++)
#define dREP(a, b, c) for(int a=(b); a>=(c); a--)

int T, D, N;

int K[10001] = {0};
int S[10001] = {0};

int main(){
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> D >> N;
		REP(i, 0, N) cin >> K[i] >> S[i];
		double mx = -1.0;
		double c = 1.0;
		REP(i, 0, N){
			c = (D-K[i])/(double(S[i]));
			mx = max(mx, c);
		}
		printf("Case #%d: %f\n", t, D/mx);
	}
	return 0;
}
