#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
template<class T> inline bool ten(T &x,const T &y){return y<x?x=y,1:0;}
template<class T> inline bool rel(T &x,const T &y){return x<y?x=y,1:0;}
int n,m,c;
int p[1005],b[1005];
int cnt[1005],sum[1005];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T=0;cin>>T;
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d: ",qi);
		scanf("%d%d%d",&n,&c,&m);
		memset(cnt,0,sizeof(cnt));
		memset(sum,0,sizeof(sum));
		for(int i=1;i<=m;i++)
			scanf("%d%d",p+i,b+i),cnt[b[i]]++,sum[p[i]]++;
		int w=0;
		for(int i=1;i<=c;i++)
			w=max(w,cnt[i]);
		for(int i=1;i<=n;i++)
			sum[i]+=sum[i-1],w=max(w,(sum[i]-1)/i+1);
		int z=0;
		for(int i=1;i<=n;i++)
			z+=max(0,sum[i]-sum[i-1]-w);
		printf("%d %d\n",w,z);
	}
	return 0;
}

