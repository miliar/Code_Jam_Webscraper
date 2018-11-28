// Bathroom Stalls

#include <set>
#include <map>
#include <iostream>

using namespace std;

typedef unsigned long long int ll;

int main(){
	int T, t;
	cin >> T;

	for(t=0; t<T; t++){
		ll N, K;
		cin >> N >> K;

		set<ll> sizes;
		sizes.insert(N);

		map<ll, ll> amounts;
		amounts.insert(make_pair(N, 1));

		while(K!=0){
			ll largest=*(--sizes.end());
			ll amount = amounts[largest];

			if(K>amounts[largest]){
				amounts[largest]=0;
				sizes.erase(largest);

				ll c1 = (largest-1)/2;
				ll c2 = (largest)/2;

				if(sizes.find(c1)==sizes.end()){
					sizes.insert(c1);
					amounts.insert(make_pair(c1, amount));
				}else{
					amounts[c1]+=amount;
				}

				if(sizes.find(c2)==sizes.end()){
					sizes.insert(c2);
					amounts.insert(make_pair(c2, amount));
				}else{
					amounts[c2]+=amount;
				}

				K-=amount;
			}else{
				amounts[largest]-=K;
				K=0;
			}
		}

		ll largest = *(--sizes.end());
		largest--;

		cout << "Case #" << (t+1) << ": " << ((largest+1)/2) << " " << (largest/2) << endl; 
	}
}