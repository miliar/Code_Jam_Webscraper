#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
#define FI first
#define SE second
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int cas,Ac,Aj,ans,task[1500],tc[1500],td[1500],tj[1500],tk[1500];
int f[1500][1500][2];
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
		scanf("%d%d",&Ac,&Aj);
		memset(task,-1,sizeof(task));
		rep(i,0,Ac){
			scanf("%d%d",&tc[i],&td[i]);
			rep(j,tc[i]+1,td[i]+1)task[j]=0;
		}
		rep(i,0,Aj){
			scanf("%d%d",&tj[i],&tk[i]);
			rep(j,tj[i]+1,tk[i]+1)task[j]=1;
		}
		memset(f,0x3f,sizeof(f));
		f[0][0][0]=0;
		rep(i,1,1440+1){
			rep(j,0,i+1){
				if(task[i]!=0  && j>0){
					f[i][j][0]=min(f[i-1][j-1][0],f[i-1][j-1][1]+1);
				}
				if(task[i]!=1){
					f[i][j][1]=min(f[i-1][j][1],f[i-1][j][0]+1);
				}
			}
		}
		ans=min(f[1440][720][0],f[1440][720][1]+1);
		//cerr<<f[1440][720][0]<<" "<<f[1440][720][1]<<endl;
		
		
		memset(f,0x3f,sizeof(f));
		f[0][0][1]=0;
		rep(i,1,1440+1){
			rep(j,0,i+1){
				if(task[i]!=0 && j>0){
					f[i][j][0]=min(f[i-1][j-1][0],f[i-1][j-1][1]+1);
				}
				if(task[i]!=1){
					f[i][j][1]=min(f[i-1][j][1],f[i-1][j][0]+1);
				}
			}
		}
		ans=min(ans,min(f[1440][720][0]+1,f[1440][720][1]));
		//cerr<<f[1440][720][0]<<" "<<f[1440][720][1]<<endl;
		//cerr<<"spa "<<f[1][0][1]<<endl;
		printf("%d\n",ans);
	}
	return 0;
}