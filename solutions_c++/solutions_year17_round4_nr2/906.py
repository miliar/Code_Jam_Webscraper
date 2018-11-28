#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
#define FI first
#define SE second
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int n,t,cas,ans,prmo,c,m,pos,per,ty;
int res[1100],lct[1100],ct[1100][1100],j;

int main(){
#ifdef AKAISORA
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		printf("Case #%d: ",t);
		scanf("%d %d %d",&n,&c,&m);
		memset(ct,0,sizeof(ct));
		memset(lct,0,sizeof(lct));
		rep(i,0,m){
			scanf("%d %d",&pos,&per);
			ct[per-1][lct[per-1]++]=pos;
		}
		rep(i,0,c)sort(ct[i],ct[i]+lct[i]);
		ans=0;
		j=0;
		rep(i,0,lct[0]){
			while(j<lct[1] && ct[1][j]<=ct[0][i])j++;
			if(j<lct[1]){
				ans++;
				ct[0][i]=-1;ct[1][j]=-1;
			}
			else break;
		}
		j=0;
		rep(i,0,lct[1]){
			if(ct[1][i]==-1)continue;
			while(j<lct[0] && ct[0][j]<=ct[1][i])j++;
			if(j<lct[0]){
				ans++;
				ct[1][i]=-1;ct[0][j]=-1;
			}
			else break;
		}
		
		memset(res,0,sizeof(res));
		rep(i,0,c)rep(j,0,lct[i])if(ct[i][j]!=-1)res[i]++;
		prmo=0;
		if(res[0]==0 || res[1]==0){
			ans+=res[0]+res[1];
		}
		else{
			ty=-1;
			rep(j,0,lct[0])if(ct[0][j]!=-1)ty=ct[0][j];
			if(ty==1){
				ans+=res[0]+res[1];
			}
			else{
				ans+=max(res[0],res[1]);
				prmo=min(res[0],res[1]);
			}
		}
		printf("%d %d\n",ans,prmo);
	}
	return 0;
}