#include <iostream>
#include <set>
using namespace std;
typedef long long ll;

int main(){
	ll tc;
	cin >> tc;
	for (ll t=1;t<=tc;t++){
		ll y, z, n, k;
		multiset<ll> ms;
		cin >> n >> k;
		
		ms.insert(n);
		while (k--){
			multiset<ll>::iterator it = ms.end();
			--it;
			y= *it /2;
			z= (*it-1) /2;
			ms.erase(it);
			if (y>0) ms.insert(y);
			if (z>0) ms.insert(z);
		}
		cout << "Case #" << t << ": "<< y << " " << z << endl;
	}
	return 0;
}
