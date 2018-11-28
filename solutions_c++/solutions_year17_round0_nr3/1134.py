#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

void insertAta(vector<ll>& value, vector<ll>& count, ll v, ll vfreq) {
	int index = -1;
	for(int i=0; i<value.size(); i++) {
		if( value[i]==v ) {
			index = i;
			break;
		}
	}
	
	if(index==-1) {
		value.push_back( v );
		count.push_back( vfreq );
	} else {
		count[index] += vfreq;
	}
}

int main() {
	int t; cin >> t;
	for(int c=1; c<=t; c++) {
		ll n, k; cin >> n >> k;
		
		ll height = 1;
		while( !( k < ( 1ull << height ) ) ) {
			height++;
		}
		ll width = k - (1ull << (height-1));
		vector<ll> values;
		vector<ll> count;
		values.push_back( n );
		count.push_back(1);
		values.push_back( -1 );
		count.push_back(0);
		for(int i=0; i<height-1; i++) {
			vector<ll> tempValues;
			vector<ll> tempCount;
			
			for(int i=0; i<values.size(); i++) {
				ll curr = values[i];
				ll freq = count[i];
				
				if(curr == -1) continue;
				
				ll temp = curr-1;

				bool odd = (temp%2==1);
				ll min = temp/2l;
				ll max = min + (odd?1:0);
				insertAta( tempValues, tempCount, min, freq );
				insertAta( tempValues, tempCount, max, freq );
			}
			
			if( tempValues.size() < 2 ) {
				tempValues.push_back(-1);
				tempCount.push_back(0);
			}
			values = vector<ll>( tempValues );
			count = vector<ll>( tempCount );
		}
		
		ll min, max, cmin, cmax;
		if(values[0] > values[1]) {
			min = values[1];
			cmin = count[1];
			
			max = values[0];
			cmax = count[0];
		} else {			
			min = values[0];
			cmin = count[0];
			
			max = values[1];
			cmax = count[1];
		}
		
		ll ans;
		if(width < cmax) {
			ans = max;
		} else {
			ans = min;
		}
		
		ll rem = ans-1;
		bool odd = (rem%2==1);
		min = rem/2l;
		max = min + (odd?1:0);
		cout << "Case #" << c << ": " << max << " " << min << endl;
	}
}