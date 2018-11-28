#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int l = 1; l <= T; l++){
		cout << "Case #" << l << ": ";

		ll D;
		int N;
		cin >> D >> N;
		ll a = 0LL, b = 1LL;
		while(N--){
			ll ki, vi;
			cin >> ki >> vi;
			ll a1, b1;
			a1 = (D - ki);
			b1 = vi;

			if(a1*b > a*b1)
				a = a1, b = b1;
		}
		double resp = (double)(D*b) / (double)(a);

		cout << fixed << setprecision(8) << resp << "\n";
	}

	return 0;
}