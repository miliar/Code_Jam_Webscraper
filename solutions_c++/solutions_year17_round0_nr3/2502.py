#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <cstdio>
using namespace std;
typedef long long LL;

int T;
LL n,k,ans,aa,bb,ra,rb;
map<LL,LL> mp;

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		scanf("%lld %lld",&n,&k);
		mp.clear();
		ans=n;
		ra=rb=n/2;
		if(n%2==0) ra--;
		mp[ra]++;mp[rb]++;
		k--;
		while(k>0) {
			k-=mp[rb];ans=rb;
			if(k<=0) break;
			if(ra!=rb) {
				k-=mp[ra];ans=ra;
				if(k<=0) break;
			}
			if(ra==rb) {
				if(ra%2==0) {
					aa=ra/2-1;
					bb=ra/2;
				}
				else
					aa=bb=ra/2;
				mp[aa]+=mp[ra];
				mp[bb]+=mp[ra];
				ra=aa;rb=bb;
				continue;
			}
			if(ra%2==0) {
				aa=ra/2-1;
				bb=ra/2;
				mp[aa]+=mp[ra];
				mp[bb]+=mp[ra]+mp[rb]*2;
				ra=aa;rb=bb;
			}
			else {
				aa=ra/2;
				bb=ra/2+1;
				mp[aa]+=mp[ra]*2+mp[rb];
				mp[bb]+=mp[rb];
				ra=aa;rb=bb;
			}
		}
		aa=bb=ans/2;
		if(ans%2==0) bb--;
		printf("Case #%d: %lld %lld\n",t,aa,bb);
	}
}