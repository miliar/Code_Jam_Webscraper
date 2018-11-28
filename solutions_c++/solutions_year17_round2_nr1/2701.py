#include <bits/stdc++.h>
using namespace std;

int T;

int main() {
	cin>>T;
	for (int t=0; t<T; t++) {
		double D, p, v, tempo=0;
		int N;
		cin >> D >> N;
		for (int i=0; i<N; ++i){
			cin >> p >> v;
			tempo = max(tempo, (D-p)/v);
		}
		
		cout<<"Case #"<<t+1<<": ";
		printf("%.10lf\n", D/tempo);
	}
	return 0;
}
