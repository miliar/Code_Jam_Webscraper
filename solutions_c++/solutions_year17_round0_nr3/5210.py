#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<cstring>
#include<cstdio>
#include <functional>
#include <numeric>
#include<cassert>
using namespace std;

#define LARGE

#ifdef SMALL_1
	string in_file = "c_small_2.in";
	string out_file = "c_small_2.out";
#endif

#ifdef SMALL_2
	string in_file = "c_small_2_real.in";
	string out_file = "c_small_2_real.out";
#endif

#ifdef LARGE
	string in_file = "c_large.in";
	string out_file = "c_large.out";
#endif

int main() {
	freopen(in_file.c_str(), "r", stdin);
	freopen(out_file.c_str(), "w", stdout);

	int t;
	cin>>t;
	for(int tt=1; tt<=t; tt++) {
		unsigned long long n, k, s=1;
		cin>>n>>k;
		map<unsigned long long, unsigned long long> m;
		m[n] = 1;
		for(; s<k; k-=s, s<<=1) {
			map<unsigned long long, unsigned long long> mm;
			for(auto x : m) {
				assert(x.first > 0);
				if(x.first%2) {
					mm[x.first>>1] += m[x.first]*2;
				} else {
					mm[x.first>>1] += m[x.first];
					mm[x.first/2-1] += m[x.first];
				}
			}
			m = mm;
		}
		unsigned long long ans = 0;
		for(auto it = m.rbegin(); it != m.rend(); it++) {
			if(it->second >= k) {
				ans = it->first;
				break;
			}
			k -= it->second;
		}
		assert(ans != 0);
		cout << "Case #"<<tt<<": "<<ans/2<<" "<<(ans-1)/2<<endl;
	}

	return 0;
}
