#include <bits/stdc++.h>

using namespace std;

int tests;
long long n;
int arr[20], sz;

int is_tidy(long long n) {
	int last = 9;
	while (n) {
		int p = n % 10LL;
		if (p > last) return 0;
		n /= 10;
		last = p;
	}
	return 1;
}

int main() 
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	
	freopen("b-input-large.in", "r", stdin);
	freopen("b-output-large.out", "w", stdout);
	
	
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		cin >> n;
		
		cout << "Case #" << test << ": ";
		if (is_tidy(n)) cout << n << endl;
		else {
			long long ans1 = 0;
			
			sz = 0;
			while (n) {
				arr[sz++] = n % 10LL;
				n /= 10;
			}
			for (int i = sz - 1; i > 0 && i < sz;) {
				if (arr[i] > arr[i - 1]) {
					--arr[i];
					for (int j = i - 1; j >= 0; --j) arr[j] = 9;
					++i;
					continue;
				} 
				--i;
			}		
			--sz;
			while (arr[sz] == 0) --sz;
			for (int i = sz; i >= 0; --i) ans1 = ans1 * 10LL + arr[i] * 1LL;
			cout << ans1 << endl;
		}
		
	}
	return 0;
}
