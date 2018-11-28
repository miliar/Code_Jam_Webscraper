#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
	long long T;
	cin >> T;
	for (long long t = 0; t < T; t++){
		if (t != 0) cout << endl;
		long long N, K;
		cin >> N >> K;
		cout << "Case #" << t + 1 << ": ";
		long long max=N/2, cmax = 1, min=N/2-((N+1)%2), cmin = 1;
		if (K == 1){
			cout << N / 2 << " " << N / 2 - ((N + 1) % 2);
			continue;
		}
		while ((cmax+cmin)*2-1 < K){
			long long m1 = max / 2,cm1=cmax, m2 = min / 2 - ((min + 1) % 2),cm2=cmin;
			if (max % 2 == 1) cm1 += cmax;
			if (min % 2 == 0) cm1 += cmin;
			if (max % 2 == 0) cm2 += cmax;
			if (min % 2 == 1) cm2 += cmin;
			cmax = cm1;
			cmin = cm2;
			max = m1;
			min = m2;
		}
		long long c = 1;
		while (K - c > 0){
			K -= c;
			c *= 2;
		}
		if (K <= cmax){
			cout << max/2 <<" "<< (max/2) - ((max + 1) % 2);
		}
		else cout << min/2 <<" "<< (min/2) - ((min + 1) % 2);
	}
	long long de;
	cin >> de;
}