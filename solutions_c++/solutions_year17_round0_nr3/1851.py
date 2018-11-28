#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <vector>
#include <cstdint>

using namespace std;

int main() {
	int cases;
	
	cin >> cases;
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": "; 
		int64_t N, K;
		cin >> N >> K;
		
		using P = pair<int64_t,int64_t>;
		vector<P> v = { { N, 1 } };
		vector<P> w;
		int64_t free = -1;
		
		while(true) {
			bool done = false;
			for( const auto& x : v ) {
				if( x.second >= K ) {
					free = x.first;
					done = true;
					break;
				}
				K -= x.second;
			}
			if( done ) break;
			
			w.clear();
			for( const auto& x : v ) {
				w.push_back( { (x.first-1)/2, x.second } );
				w.push_back( { x.first/2, x.second } );
			}
			sort( w.begin(), w.end(), greater<P>() );
			v.clear();
			v.push_back( w[0] );
			for( size_t i = 1; i < w.size(); ++i ) {
				if( w[i].first == v.back().first ) {
					v.back().second += w[i].second;
				} else {
					v.push_back( w[i] );
				}
			}
			assert( v.size() <= 2 );
		}
		assert( free >= 1 );
		--free;
		cout << max(free/2,(free+1)/2) << ' ' << min(free/2,(free+1)/2) << endl;
	}
	return 0;	
}
