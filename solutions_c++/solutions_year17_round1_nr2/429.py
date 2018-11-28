#include <cstdio>
#include <cmath>
#include <algorithm>
#define LL long long
using namespace std;

const int Maxn=50;

int N,P;
LL req[Maxn+5];
LL pkg[Maxn+5][Maxn+5];
int pos[Maxn+5];

inline void solve(int T){
	scanf("%d%d",&N,&P);
	for (int i=1;i<=N;i++) scanf("%lld",&req[i]);
	for (int i=1;i<=N;i++) for (int j=1;j<=P;j++) scanf("%lld",&pkg[i][j]);
	for (int i=1;i<=N;i++) sort(pkg[i]+1,pkg[i]+P+1);

	int idx=1;
	for (int i=2;i<=N;i++) if (pkg[i][P]/req[i]>pkg[idx][P]/req[idx]) idx=i;
	for (int i=1;i<=N;i++) pos[i]=1;

	LL lim=pkg[idx][P]/req[idx]+5LL;
	LL Ans=0;

	for (LL now=1;now<=lim;now++){
		bool flag=true;
		while(flag){
			for (int i=1;i<=N;i++){
				LL dLim=req[i]*now,uLim=req[i]*now;
				dLim=ceil((double)dLim*(double)(0.9));
				uLim=floor((double)uLim*(double)(1.1));
				while(pos[i]<=P && pkg[i][pos[i]]<=uLim && pkg[i][pos[i]]<dLim) pos[i]++;
				if (pos[i]>P || pkg[i][pos[i]]>uLim) flag=false;
			}
			if (flag){
				Ans++;
				for (int i=1;i<=N;i++) pos[i]++;
			}
		}
	}

	printf("Case #%d: %lld\n",T,Ans);
}

int main(){
	freopen("B-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T=0;scanf("%d",&T);
	for (int i=1;i<=T;i++) solve(i);
	return 0;
}