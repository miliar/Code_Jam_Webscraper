#include<iostream>
#include<map>
using namespace std;

int _, T;

map<long long, long long> mp;
map<long long, long long>::iterator it;

int main() {
	cin>>_;
	for(int T=1; T<=_; T++) {
		long long x, k;
		cin>>x>>k;
		k--;
		
		mp.clear();
		mp[x] = 1;
		while(k) {
			it = mp.end(); it--;
			long long v = (*it).first, det = min((*it).second, k);
			long long l = (v-1)/2;
			long long r = (v-1)-l;
			mp[l]+=det;
			mp[r]+=det;
			if (det < (*it).second) (*it).second -= det;
			else mp.erase(it);
			k-=det;
		}
		it = mp.end(); it--;
		long long v = (*it).first;
		long long mi = (v-1)/2;
		long long ma = (v-1)-mi;
		cout<<"Case #" << T << ": "<<ma<<' '<<mi<<endl;
	}
	
	return 0;
}