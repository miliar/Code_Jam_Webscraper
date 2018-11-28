#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <string>
#include <bitset>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <sstream>
#include <stack>
#include <iomanip>
using namespace std;
#define pb push_back
#define mp make_pair
typedef pair<int,int> pii;
typedef long long ll;
typedef double ld;
typedef vector<int> vi;
#define fi first
#define se second
#define fe first
#define FO(x) {freopen(#x".in","r",stdin);freopen(#x".out","w",stdout);}
#define Edg int M=0,fst[SZ],vb[SZ],nxt[SZ];void ad_de(int a,int b){++M;nxt[M]=fst[a];fst[a]=M;vb[M]=b;}void adde(int a,int b){ad_de(a,b);ad_de(b,a);}
#define Edgc int M=0,fst[SZ],vb[SZ],nxt[SZ],vc[SZ];void ad_de(int a,int b,int c){++M;nxt[M]=fst[a];fst[a]=M;vb[M]=b;vc[M]=c;}void adde(int a,int b,int c){ad_de(a,b,c);ad_de(b,a,c);}
#define es(x,e) (int e=fst[x];e;e=nxt[e])
#define esb(x,e,b) (int e=fst[x],b=vb[e];e;e=nxt[e],b=vb[e])
#define VIZ {printf("digraph G{\n"); for(int i=1;i<=n;i++) for es(i,e) printf("%d->%d;\n",i,vb[e]); puts("}");}
#define VIZ2 {printf("graph G{\n"); for(int i=1;i<=n;i++) for es(i,e) if(vb[e]>=i)printf("%d--%d;\n",i,vb[e]); puts("}");}
#define SZ 666666
int T,ac,aj,b[SZ];
const int mx=24*60;
int minn[mx+3][mx+3][2];
void sol()
{
	memset(b,0,sizeof(b));
	scanf("%d%d",&ac,&aj);
	for(int i=1;i<=ac;i++)
	{
		int l,r;
		scanf("%d%d",&l,&r);
		for(int p=l;p<r;p++) b[p]=1;
	}
	for(int i=1;i<=aj;i++)
	{
		int l,r;
		scanf("%d%d",&l,&r);
		for(int p=l;p<r;p++) b[p]=2;
	}
	int ans=1e9;
	for(int s=0;s<2;s++)
	{
	memset(minn,127/3,sizeof(minn));
	for(int i=0;i<mx;i++)
	{
		for(int k=0;k<=mx;k++)
		{
		//for(int j=0;j<2;j++)
		if(k)
		{
			if(b[i]!=1)
			{
			int& c=minn[i][k][0];
			if(i) c=min(c,minn[i-1][k-1][1]+1),
			c=min(c,minn[i-1][k-1][0]);
			else if(k==1&&!s) c=0;
			}
		}
		{
			if(b[i]!=2)
			{
			int& c=minn[i][k][1];
			if(i) c=min(c,minn[i-1][k][0]+1),
			c=min(c,minn[i-1][k][1]);
			else if(!k&&s) c=0;
			}
		}
		}
	}
	ans=min(ans,minn[mx-1][mx/2][s]);
	ans=min(ans,minn[mx-1][mx/2][!s]+1);
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)cerr<<i<<"\n",printf("Case #%d: ",i),sol();
}

