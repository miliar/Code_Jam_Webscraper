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

bool tidy(unsigned long long x) {
	int p = 9;
	while(x) {
		int c = x%10;
		if(c > p) return false;
		p = c;
		x/=10;
	}
	return true;
}

int main() {

#ifdef SMALL
	freopen("b_small.in", "r", stdin);
	freopen("b_small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("b_large.in", "r", stdin);
	freopen("b_large.out", "w", stdout);
#endif

#ifdef LOCAL
	freopen("b.in", "r", stdin);
#endif

	int t;
	cin>>t;
	for(int tt=1; tt<=t; tt++) {
		unsigned long long n;
		cin>>n;
		vector<unsigned long long> all;
		all.push_back(n);
		vector<int> v;
		while(n) {
			v.push_back(n%10);
			n/=10;
		}
		reverse(v.begin(), v.end());
		if(v.size() > 1) {
			all.push_back(0);
			for(int i=0;i+1<v.size();i++) {
				all.back() = all.back()*10+9;
			}
		}
		for(int i=0;i+1<v.size();i++) {
			vector<int> vv = v;
			if(v[i] <= 1) {
				continue;
			}
			unsigned long long x = 0;
			for(int j=0;j<i;j++)
				x = x*10+v[j];
			x = x*10+v[i]-1;
			for(int j=i+1;j<v.size();j++)
				x = x*10+9;
			all.push_back(x);
		}
		sort(all.rbegin(), all.rend());
		unsigned long long ans = 0;
		for(auto x : all) {
			if(tidy(x)) {
				ans = x;
				break;
			}
		}
		assert(ans);
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}

	return 0;
}
