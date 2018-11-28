#include<bits/stdc++.h>
using namespace std;
#define ALL(v) (v).begin(),(v).end()
int main() {
	int T; cin >> T;
	for(int tc=1;tc<=T;tc++) {
		int W; cin >> W;
		int n; cin >> n;
		static int K[1000],S[1000];
		static double tend[1000];
		for(int i=0;i<n;i++){
			cin >> K[i]>>S[i];
			tend[i] = (double)(W-K[i])/(double)S[i];
		}
		double t = *max_element(tend,tend+n);
		printf("Case #%d: %.9lf\n", tc, (double)W / (double)t);
	}
}
