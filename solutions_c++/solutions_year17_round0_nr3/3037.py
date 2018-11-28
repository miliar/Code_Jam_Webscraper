#include <bits/stdc++.h>
using namespace std;
long long T, N, K, parity, flag;
long long a[62];
int main(){
	freopen("largeQc.in", "r", stdin);
	freopen("largeQc.out", "w", stdout);
	cin >> T;
	a[0] = 1;
	for(int i = 1; i <= 60 && a[i - 1] <= 1e18; i++){
		a[i] = a[i - 1] * 2;
	}
	long long k = 0;
	for(int i = 1; i <= T; i++){
		flag = 0;
		cin >> N >> K;
		long long record = N;
		cout << "Case #" << i << ": ";
		if(K == 1){
			cout << max(N / 2, N - N / 2 - 1) << ' ' << min(N / 2, N - N / 2 - 1) << endl;
			continue;
		}
		long long num = 0;
		long long sum = 0;
		for(int j = 0; j <= 60; j++){
			sum += a[j];
			if(sum < K){
				num++;
				record -= a[j];
				k = K - sum;
			}
			else {
				break;
			}
		}
		//cout << record << ' ' << num << ' ' << k << endl;
		long long ans;
		if(k <= (record - a[num]) % (a[num])){
			ans = (record - a[num]) / (a[num]) + 1;
		}
		else ans = (record - a[num]) / (a[num]);
		long long n1 = max(ans / 2, ans - ans / 2);
		cout << n1 << ' ' << ans - n1 << endl;
	}
return 0;
}

