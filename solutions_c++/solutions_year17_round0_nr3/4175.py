#include<bits/stdc++.h>
#include<unordered_set>
#include<unordered_map>
using namespace std;

int t;

int coun;
void outt(){
	coun++;
	cout << "Case #" << coun << ": ";
}


long long int n;

map<long long int, int> mp;


int main(){
	cin >> t;
	while (t--){
		long long int k;
		scanf("%lld%lld", &n, &k);
		mp.clear();
		mp[n]++;
		outt();
		while (mp.size()){
			long long int val = (*mp.rbegin()).first;
			if (val == 0LL){
				puts("0 0");
				break;
			}
			long long int se = (*mp.rbegin()).second;
			mp.erase(val);
			if (k <= se){//cutting
				if (val & 1LL){
					long long int go = (val - 1) / 2LL;
					printf("%lld %lld\n", go, go);
					break;
				}
				else{
					long long int f1 = val / 2LL;
					long long int f2 = f1 - 1LL;
					printf("%lld %lld\n", f1, f2);
					break;
				}
			}
			else{
				k -= se;
			}
			if (val % 2LL){
				long long int go = (val - 1) / 2LL;
				mp[go] += se * 2LL;
			}
			else{
				long long int go = val / 2LL;
				mp[go] += se;
				mp[go - 1LL] += se;
			}
		}
	}
	return 0;
}