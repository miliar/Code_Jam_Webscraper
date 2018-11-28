#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

int main(){
	ios::sync_with_stdio(false);
	int t;
	uint64 k, n;
	
	cin >> t;

	for(int w = 1; w <= t; w++){
		cin >> n >> k;
		
		map < uint64, uint64 > mapa;
		map < uint64, uint64 > :: iterator it;
		mapa[n]++;
		uint64 at = 0;

		while( k ){
			it = mapa.end();
			it--;

			if( it->second >= k ){
				at = it->first;
				break;
			}
			else{
				k -= it->second;
				uint64 qt = it->second;
				at = it->first;
				mapa.erase(it);
				mapa[at>>1] += qt;
				mapa[at-((at>>1)+1)] += qt;
			}
		}
		cout << "Case #" << w << ": ";
		cout << max(at>>1, at-((at>>1)+1)) << " " << min(at>>1, at-((at>>1)+1)) << endl;
		
	}

	return 0;
}