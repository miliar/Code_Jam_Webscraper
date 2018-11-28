#include<stdio.h>
#include<string.h>
#include<set>
using namespace std;
int cnt[1111],l[1111];
int n,m;
bool ok(int x){
	int lef = 0;
	for(int i=1; i<=n; i++){
		lef += x;
		if(lef >= cnt[i])
			lef -= cnt[i];
		else
			return false;
	}
	return true;
}
int main(){
	int _,T,C;
	scanf("%d",&_);
	for(T=1; T<=_; T++){
		scanf("%d%d%d",&n,&C,&m);
		memset(cnt,0,sizeof(cnt));
		memset(l,0,sizeof(l));
		for(int i=0; i<m; i++){
			int x,y;
			scanf("%d%d",&x,&y);
			cnt[x] ++;
			l[y-1]++;
		}
		int lo = 0;
		for(int i=0; i<C; i++)
			lo = max(lo, l[i]);
		int hi = m;
		while(lo != hi){
			int mi = (lo + hi)/2;
			if(ok (mi))
				hi = mi;
			else
				lo = mi+1;
		}

		int res2 = 0, lef = 0;
		for(int i=1; i<=n; i++){
			int w = cnt[i];
			if(w <= lo) lef += lo - w; else{
				w -= lo;
				res2 += w;
				lef -= w;
			}
		}
		printf("Case #%d: %d %d\n",T,lo,res2);
	}
	return 0;
}
