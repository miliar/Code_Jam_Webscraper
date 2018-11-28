#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		ll m;
		ll smaller;
		ll numLarger;
		ll numSmaller;
		cin >> smaller >> m;
		numLarger = 0;
		numSmaller = 1;
		while(m>0){
			if(m<=numLarger){
				cout << "Case #" << i << ": " << (smaller+1)/2 << " " << smaller/2 << endl;
				m=0;
				continue;
			}
			m-=numLarger;
			if(m<=numSmaller){
				cout << "Case #" << i << ": " << smaller/2 << " " << (smaller-1)/2 << endl;
				m=0;
				continue;
			}
			m-=numSmaller;
			ll ts = ((smaller+1)/2)-1;
			ll tnl,tns;
			if(smaller%2 == 0){
				tnl = 2*numLarger + numSmaller;
				tns = numSmaller;
			}
			else{
				tnl = numLarger;
				tns = numLarger + 2*numSmaller;
			}
			smaller = ts;
			numLarger = tnl;
			numSmaller = tns;
		
		}

	}
	return 0;
}
