#include<bits/stdc++.h>


using namespace std;

const int maxn = 55;

int n,p,cas=0;

int R[maxn],Q[maxn][maxn];
int Now[maxn];

int Low(long long x){
	if(x>1e9)return 2000000;
	x*=90;
	if(x%100==0)return x/100;
	else return x/100+1;
}

int High(long long x){
	if(x>1e9)return 2000000;
	x*=110;
	if(x%100==0)return x/100;
	else return x/100;
}

void Work(){
	int ans=0;
	for(int j=1;j<=1000000;j++){
		int mn = p+1;
		for(int i=1;i<=n;i++){
			int L=Low(1LL*R[i]*j),RR=High(1LL*R[i]*j);
			int l=lower_bound(Q[i]+Now[i]+1,Q[i]+p+1,L)-Q[i];
			int r=upper_bound(Q[i]+Now[i]+1,Q[i]+p+1,RR)-Q[i]-1;
			mn=min(mn,r-l+1);
			if(!mn)break;
		}
		ans+=mn;
		for(int i=1;i<=n;i++){
			int L=Low(1LL*R[i]*j),RR=High(1LL*R[i]*j);
			int l=lower_bound(Q[i]+Now[i]+1,Q[i]+p+1,L)-Q[i];
			Now[i]=l+mn-1;
		}
	}
	printf("Case #%d: %d\n",++cas,ans);
	cerr<<cas<<endl;
}

void Init(){
	scanf("%d%d",&n,&p);
	for(int i=1;i<=n;i++)scanf("%d",&R[i]);
	for(int i=1;i<=n;i++)for(int j=1;j<=p;j++)scanf("%d",&Q[i][j]);
	for(int i=1;i<=n;i++)sort(Q[i]+1,Q[i]+p+1);
	for(int i=1;i<=n;i++)Now[i]=0;
}

int main(){
	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);
	int T;
	scanf("%d",&T);
	while(T--){
		Init();
		Work();
	}
	return 0;
}
