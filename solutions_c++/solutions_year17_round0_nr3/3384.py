#include <iostream>
#include <set>
#include <algorithm>
using namespace std;
typedef long long int ll;

int main(){
	int t;
	cin >> t;
	for(int T = 1; T <= t; T++){
		cout << "Case #" << T << ": ";
		ll n, k;
		ll xa, xb;
		multiset<ll> s;
		cin >> n;
		cin >> k;
//		if(n == k) {
//			cout << "0 0\n";
//		} else if (k > (n-1)>>1){
//			cout << "1 0\n";
//		}
//		else {
			s.insert(n);
			for(ll i = 0; i < k; i++){
				ll cur = *(--s.end());
				if(cur == 0) break;
				s.erase(--s.end());
				if(cur & 1){
					xa = cur >> 1;
					xb = cur >> 1;
					s.insert(xa);
					s.insert(xb);
				} else {
					xa = (cur-1)>>1;
					xb = cur >> 1;
					s.insert(xa);
					s.insert(xb);
				}
			}
			cout << xb << " " << xa << "\n";
//		}

	}

}

