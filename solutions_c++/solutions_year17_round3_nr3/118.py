#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	int T; cin >> T;
	for (int t=1;t<=T;t++){
		int N,K; cin >> N >> K;
		double P[N], U; cin >> U;

		for (int j=0;j<N;j++) {
			cin >> P[j];
		
		}
		sort(P,P+N);
		bool done = false;
		for (int j=1;j<N;j++){
			if (U >= (P[j]-P[j-1])*j){
				U -= (P[j]-P[j-1])*j;
				for (int k=0;k<j;k++) P[k] = P[j];
			} else {
				for (int k=0;k<j;k++) P[k] += (U/j);
				done = true;
				break;
			}
		}
	
		if (!done){
			for (int j=0;j<N;j++) {
				P[j] += (U/N);
				P[j] = min(P[j], 1.);
			}
		}
		double prob = 1.;
		for (int i=0;i<N;i++) prob*= P[i];
		printf("Case #%d: %.9lf\n", t,prob);
	}
}
