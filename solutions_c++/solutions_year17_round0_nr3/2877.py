#include <bits/stdc++.h>

using namespace std;



typedef long long ll;

ll D, n, k, m, L, a, ran, ans;

ll pot(ll a, ll b){
	ll r = 1;
	while(b){
		if(b%2==1){
			r*=a;
		}
		a*=a;
		b/=2;
	}
	return r;
}



int main(){
	int t;
	scanf("%d",&t);

	for(int caso=1; caso<=t; caso++){

		scanf("%lld %lld",&n,&k);
		

L = k;

		m = 0;

		while(L != 1){

			L = L/2;

			m++;

		}


		D = (n - pot(2,m) + 1)/pot(2,m);

		a = k - pot(2,m) + 1;

		ran = n - pot(2,m) + 1 - D*pot(2,m);

		
if(a <= ran) ans = D+1;

		else ans = D;


		cout << "Case #" << caso << ": " << ans/2 << " " << (ans-1)/2 << endl;

	}


	return 0;

}
