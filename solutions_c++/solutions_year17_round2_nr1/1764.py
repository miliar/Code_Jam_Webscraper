#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int K[1005];
int S[1005];

pair<int, int> KS[1005];

int main(){
	int T;
	cin >> T;
	int t=1;
	for(;t<=T;t++){
		int D, N;
		cin >> D >> N;
		for(int i=0;i<N;i++){
			cin >> KS[i].first >> KS[i].second;
		}
		sort(KS, KS+N);

		double tt = 0;
		for(int i=N-1;i>=0;i--){
			tt = max((double)(D-KS[i].first)/KS[i].second, tt);
		}
		printf("Case #%d: ", t);
		printf("%lf\n", D/tt);
	}
}