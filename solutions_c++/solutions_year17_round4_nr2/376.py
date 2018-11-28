#include<bits/stdc++.h>


using namespace std;

const int maxn = 1010;

int n,c,m,cas,Ans;

int sm[maxn],has[maxn],Is[maxn];

bool check(int M){
	for(int i=1;i<=n;i++)if(sm[i]>M*i)return false;
	Ans=0;
	for(int i=1;i<=n;i++)Ans+=max(0,Is[i]-M);
	return true;
}

void Work(){
	int l=0,r=m;
	for(int i=1;i<=c;i++)l=max(l,has[i]);
	while(l<r){
		int M=l+r>>1;
		if(check(M))r=M;else l=M+1;
	}
	check(l);
	printf("Case #%d: %d %d\n",++cas,l,Ans);
}

void Init(){
	scanf("%d%d%d",&n,&c,&m);
	for(int i=1;i<=n;i++)sm[i]=0;
	for(int i=1;i<=c;i++)has[i]=0;
	for(int i=1;i<=m;i++){
		int x,y;
		scanf("%d%d",&x,&y);
		has[y]++;
		sm[x]++;
	}
	for(int i=1;i<=n;i++)Is[i]=sm[i];
	for(int i=1;i<=n;i++)sm[i]+=sm[i-1];
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
