#include <iostream>

using namespace std;
const int maxn = 25;
long long n;
long long a[maxn];
long long ans[maxn];

bool check(int index){
	for (int i = index - 1; i >= 0; i--){
		if (a[i] > a[i + 1])
			return true;
		if (a[i] < a[index])
			return false;
	}
	return true;
}

long long calc(){
	int len = 0;
	long long m = n;
	while(m){
		a[len++] = m % 10;
		m /= 10;
	}
	for (int i = len - 1; i >= 0; i--){
		if (check(i))
			ans[i] = a[i];
		else{
			ans[i] = a[i] - 1;
			for (int j = i - 1; j >= 0; j--)
				ans[j] = 9;
			break;
		}
	}
	m = 0;
	for (int i = len - 1; i >= 0; i--)
		m = m * 10 + ans[i];
	return m;
}

// bool check(int x){
// 	int len = 0;
// 	while(x){
// 		a[len++] = x % 10;
// 		x /= 10;
// 	}
// 	for (int i = len - 2; i >= 0; i--)
// 		if (a[i] < a[i + 1])
// 			return false;
// 	return true;
// }

// int calc(){
// 	for (int i = n; i >= 1; i--)
// 		if (check(i))
// 			return i;

// }

int main(){
	int T;
	cin >> T;

	for (int i = 0; i < T; i++){
		cin >> n;
		printf("Case #%d: %lld\n", i + 1, calc());
		// printf("Case #%d: %d\n", i + 1, calc());
	}
	return 0;
}