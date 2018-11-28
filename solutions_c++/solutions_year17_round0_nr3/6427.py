#include <map>
#include <iostream>
#include <cstdio>

using namespace std;


int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i){
		map<long long, long long> res;
		long long n, k;
		cin >> n >> k;
		res[n] = 1;
		while(k > 0){
			n = res.rbegin()->first;
			k -= res.rbegin()->second;
			res[n / 2] += res.rbegin()->second;
			res[(n - 1) / 2] += res.rbegin()->second;
			res.erase(res.rbegin()->first);
		}
		printf("Case #%d: %lld %lld\n", i + 1, n / 2, (n - 1) / 2);
	}
}
