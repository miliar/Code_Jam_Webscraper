#include <bits/stdc++.h>
using namespace std;

#define IOS std::ios_base::sync_with_stdio(false);std:cin.tie(0);std::cout.tie(0);
typedef long long ll;
map<ll, ll> mp[100];
int main() {
	int casos;
	cin >> casos;

	ll n, k;
	for(int caso = 1; caso <= casos; caso++) {
		for(int i = 0; i < 100; i++) 
			mp[i].clear();
		
		cin >> n >> k;
		cout << "Case #" << caso << ": ";

		if(k == 1) {
			cout << n/2 << " " << (n-1)/2 << endl;
			continue;
		}

 		mp[0][-n] = 1;
		ll cant = 1;
		int last = 0;
		for(int i = 1; k - cant > 0; i++, k -= cant, cant*=2) {
			auto it = mp[i-1].begin();
			last = i;

			for(; it != mp[i-1].end(); it++) {
				mp[i][it->first/2] += it->second;
				mp[i][(it->first+1)/2] += it->second;
			}
		}
		//cout << last << "---" << endl; 
		auto it = mp[last].begin();
		for(; it != mp[last].end(); it++) {
			if(k<=it->second) {
				//cout << "deb: " << -it->first<< " " << it->second <<endl;
				cout << (-it->first)/2 << " " << ((-it->first)-1)/2 << endl;
				break;
			}
			k -= it->second;
		}




	}


	return 0;
}
