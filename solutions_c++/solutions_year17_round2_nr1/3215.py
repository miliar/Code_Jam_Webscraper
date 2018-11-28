#include <bits/stdc++.h>

using namespace std;

void solve() {
	vector<long double> horses;
	long D, N;
	scanf("%ld %ld\n", &D, &N);
	for (long i = 0; i < N; i++) {
		long K, S;
		scanf("%ld %ld\n", &K, &S);
		horses.push_back((D-K)/(long double)S);
	}
	long double max = 0;
	for (long i = 0; i < N; i++) {
		if (max < horses[i])
			max = horses[i];
	}	
	for (long i = 0; i < N; i++) {
	}

	printf("%Lf\n", (long double)D/max);


}

int main(){
	int T;
	cin >> T;
	for (int i = 1; i<=T; i++) {
		printf("Case #%d: ", i);
		solve();			
	}
	return 0;
}