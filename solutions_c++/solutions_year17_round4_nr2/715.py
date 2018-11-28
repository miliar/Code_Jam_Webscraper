#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>

using namespace std;

int TT,n,c,m,tot,xx,yy,l,r,mid;
int vis[1111],done[1111];
vector<pair<int, int> > ticket;

bool check(int lim){
	memset(done,0,sizeof done);
	for	(int rpt = 1;rpt <= lim; ++rpt){
		memset(vis,0,sizeof vis);
		int curpos = 1;
		for	(int i=0;i<m;++i)
			if	(!done[i])
				if	(ticket[i].first >= curpos && vis[ticket[i].second]==0){
					done[i] = 1;
					vis[ticket[i].second] = 1;
					curpos++;
				}
	}
	for	(int i=0;i<m;++i)
		if	(!done[i])	return	false;
	return	true;
}

int main(){
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&TT);
	for	(int T=1;T<=TT;++T){
		scanf("%d%d%d",&n,&c,&m);
		ticket.clear();
		for	(int i=1;i<=m;++i){
			scanf("%d%d",&xx,&yy);
			ticket.push_back(make_pair(xx,yy));
		} 
		sort(ticket.begin(),ticket.end());
		l = 1; r = m;
		while (l < r){
			mid = (l + r) / 2;
			if	(check(mid))	r = mid;
			else l = mid + 1;
		}
		memset(vis,0,sizeof vis);
		for	(int i=0;i<m;++i)
			vis[ticket[i].first]++;
		tot = 0;
		for	(int i=1;i<=n;++i)	tot += max(0, vis[i] - l);
		printf("Case #%d: %d %d\n", T, l, tot);
	}
}
