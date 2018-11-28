#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
typedef long long ll;

int main() {
	int T;
	cin>>T;
	for (int t=1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		ll n, k;
		cin>>n>>k;
		map<ll, ll> pieces;
		pieces[n] = 1;
		while(1) {
			map<ll, ll>::reverse_iterator rit = pieces.rbegin();
			n = rit->first;
			ll count = rit->second;
			if (k <= count) {
				cout << n/2 << " " << (n-1)/2 << endl;
				break;
			}
			pieces.erase(n);
			k -= count;
			pieces[(n-1)/2] += count;
			pieces[n/2] += count;
		}
	}
	return 0;
}