#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
#define FI first
#define SE second
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int n,p,x,t,cas,ans,np;
int cnt[5];

int main(){
#ifdef AKAISORA
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		printf("Case #%d: ",t);
		scanf("%d %d",&n,&p);
		memset(cnt,0,sizeof(cnt));
		rep(i,0,n){
			scanf("%d",&x);
			cnt[x%p]++;
		}
		ans=cnt[0];
		if(p==2){	
			np=cnt[1]/2;		//1+1
			ans+=np;
			cnt[1]-=2*np;
			
			if(cnt[1])ans++;
		}
		else if (p==3){
			np=min(cnt[1],cnt[2]);    //1+2
			ans+=np;
			cnt[1]-=np;cnt[2]-=np;

			np=cnt[2]/3;			//2+2+2
			ans+=np;
			cnt[2]-=np*3;
			
			np=cnt[1]/3;			//1+1+1
			ans+=np;
			cnt[1]-=np*3;
			
			if(cnt[1] || cnt[2])ans++;
		}
		else if(p==4){
			np=min(cnt[1],cnt[3]);   //1+3
			ans+=np;
			cnt[1]-=np;cnt[3]-=np;
			
			np=cnt[2]/2;
			ans+=np;
			cnt[2]-=np*2;
			
			np=min(cnt[1]/2,cnt[2]);
			ans+=np;
			cnt[1]-=np*2;cnt[2]-=np;
			
			np=cnt[1]/4;
			ans+=np;
			cnt[1]-=np*4;

			np=cnt[3]/4;
			ans+=np;
			cnt[3]-=np*4;
			
			if(cnt[1] || cnt[2] || cnt[3])ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}