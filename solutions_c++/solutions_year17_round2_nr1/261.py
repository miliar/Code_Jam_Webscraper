#include <bits/stdc++.h>
using namespace std;
double K[1111], S[1111];
int main(){
	int t = 0, cs = 0;
	cin >> t;
	while(t--){
		int N;
		double D;
		++cs;
		cout << "Case #" << cs << ": ";
		cin >> D >> N;
		for(int i=1; i<=N; ++i){
			cin >> K[i] >> S[i];
		}
		double ans = 100000000000000;
		for(int i=1; i<=N; ++i){
			double val =  ((D * S[i]) / (D - K[i]));
			ans = min(ans, val);
		}
		printf("%0.6lf\n", ans);
	}
}