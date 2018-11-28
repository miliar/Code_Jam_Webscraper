#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
#define FI first
#define SE second
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int n,p,cas,t,ans;
int r[60],pos[60],q[60][60];
bool chs[60][60];
int main(){
#ifdef AKAISORA
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		printf("Case #%d: ",t);
		scanf("%d %d",&n,&p);
		rep(i,0,n)scanf("%d",&r[i]);
		rep(i,0,n)rep(j,0,p)scanf("%d",&q[i][j]);
		memset(pos,0,sizeof(int)*(n+5));
		rep(i,0,n)sort(q[i],q[i]+p);
		ans=0;
		memset(chs,0,sizeof(chs));
		rep(serv,1,1000010){
			if(ans>=p)break;
			while(true){
				memset(pos,-1,sizeof(pos));
				rep(i,0,n){
					rep(j,0,p){
						if(!chs[i][j] && q[i][j]>=((ll)r[i]*serv*9+10-1)/10 && q[i][j]<=(ll)r[i]*serv*11/10){
							pos[i]=j;
							//cout<<serv<<" "<<r[i]<<" "<<q[i][j]<<endl;
							break;
						}
					}
				}
				bool suss=true;
				rep(i,0,n)if(pos[i]==-1){suss=false;break;}
				if(!suss)break;
				else{
					rep(i,0,n)chs[i][pos[i]]=true;
					ans++;
				}
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}