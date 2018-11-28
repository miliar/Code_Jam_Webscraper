#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int tc=1; tc <= T; ++tc){
		int N,D;
		cin >> D >> N;
		double t = 0;
		for(int i=0; i<N; ++i){
			double K, S;
			cin >> K >> S;
			double ct = (D - K) / S;
			t = max(t, ct);
		}
		printf("Case #%d: %lf\n", tc, D/t);
	}
}