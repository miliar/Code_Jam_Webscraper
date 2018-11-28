#include <bits/stdc++.h>
#define fr(x) scanf("%lld", &x)
#define int long long
using namespace std;

map<int,int> m;

signed main(){
	int t, n, k;
	fr(t);

	for(int t1=1; t1<=t ;++t1){
		fr(n);
		fr(k);

		m.clear();
		m[n]=1;
		
		while(1){
			int key=m.rbegin()->first;
			k-=m[key];
			if(key&1){
				m[key>>1]+=(2*m[key]);
			}
			else{
				m[key>>1]+=m[key];
				m[(key-1)>>1]+=m[key];

			}
			m.erase(key);
			if(k<=0){
				printf("Case #%lld: %lld %lld\n", t1, (key>>1), ((key-1)>>1));
				break;
			}
		}
	}
	return 0;
}