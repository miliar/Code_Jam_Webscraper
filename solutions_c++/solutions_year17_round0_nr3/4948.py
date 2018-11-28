#include <bits/stdc++.h>
using namespace std;

long long v, n, k, m, len, alpha, ranv1, r;
int t, nc=1;

int main(){

	cin >> t;
	while(t--){
		cin >> n >> k;		

		len = k;
		m = 0;
		while(len != 1){
			len >>= 1;
			m++;
		}

		v = (n - (1<<m) + 1)/(1<<m);
		alpha = k - (1<<m) + 1;
		ranv1 = n - (1<<m) + 1 - v*(1<<m);
		
		if(alpha <= ranv1) r = v+1;
		else r = v;

		cout << "Case #" << nc++ << ": " << r/2 << " " << (r-1)/2 << endl;
	}

	return 0;
}
