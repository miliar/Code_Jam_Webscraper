#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;

double getTime(int D, int S, int K){
	return (((double)D)-((double)S))/((double)K);
}

int main(){
	int t, T;
	cin >> T;

	for(t=0; t<T; t++){
		int D, N;
		cin >> D >> N;

		vector<pair<int, int> > X;
		int i;

		for(i=0; i<N; i++){
			int Ki, Si;
			cin >> Ki >> Si;

			X.push_back(make_pair(Ki, Si));
		}

		double lowest=getTime(D, X[0].first, X[0].second);

		for(i=1; i<X.size(); i++){
			double tm=getTime(D, X[i].first, X[i].second);

			if(tm>lowest){
				lowest=tm;
			}
		}

		printf("Case #%d: %.6lf\n", t+1, ((double)D)/lowest);
	}
}