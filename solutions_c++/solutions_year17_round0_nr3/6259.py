#include <iostream>
#include <list>
#include <map>
using namespace std;

int main() {
	long long t,n,k,lc,rc;
	cin>>t;
	for (long long ti = 1; ti <= t; ++ti) {
		cout<<"Case #"<<ti<<": ";
		cin>>n>>k;
		map<long long, long long,greater<long long> > mx;
		map<long long, long long,greater<long long> >::iterator it;
		mx[n] = 1;
		long lc, rc;
		for (int i = 0; i < k; ++i) {
			it = mx.begin();
			long long s = it->first - 1;
			long long h = s / 2;
//			cout<<s<<"-"<<h<<"\n";
			lc = h, rc = s-h;
			if (h) mx[h]++;
			if (s-h) mx[s-h]++;
			if (it->second == 1) mx.erase(it->first);
			else mx[it->first]--;
		}
		it = mx.begin();
		
		if (lc>rc) cout<<lc<<" "<<rc;
		else cout<<rc<<" "<<lc;
//		while(it != mx.end()) {
//			cout<<it->first<<"->"<<it->second<<endl;
//			++it;
//		}
		
		cout<<"\n";
	}
}
