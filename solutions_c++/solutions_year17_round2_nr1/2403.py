#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;

int main(){
	ll t, d, n, k, s;
	cin >> t;
	cout << setprecision(20);
	for(int i = 0; i < t; i++){
		cin >> d >> n;
		ld max = 1e-11;
		for(int j = 0; j < n; j++){
			cin >> k >> s;
			if((ld)(d-k)/(ld)s > max){
				max = (ld)(d-k)/(ld)s;
			}
		}

		cout << "Case #" << i+1 << ": " << d/max << endl;
	}
	return 0;
}