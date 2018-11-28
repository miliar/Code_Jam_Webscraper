#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
map<LL, LL> mm;
pair<LL, LL> work(LL n, LL k){
	mm.clear();
	mm[n] = 1;
	while(k > 0){
		map<LL, LL>::iterator it = mm.end();
		it--;
		LL len = it -> first;
		LL num = it -> second;
		len--;
		mm.erase(it);
		LL r = len / 2;
		LL l = len - r;
		//cout<<len<<' '<<num<<' '<<k<<' '<<l<<' '<<r<<endl;
		if(num >= k) return make_pair(l, r);
		mm[l] += num;
		mm[r] += num;
		k -= num;
	}
}
int main(){
	freopen("C_large.in", "r", stdin);
	freopen("C_large.out", "w", stdout);
	int T;
	cin>>T;
	for(int ii = 1; ii <= T; ii++){
		LL n, k;
		cin>>n>>k;
		printf("Case #%d: ",ii);
		pair<LL, LL> p = work(n,k);
		cout<<p.first<<' '<<p.second<<endl;
	}
}
