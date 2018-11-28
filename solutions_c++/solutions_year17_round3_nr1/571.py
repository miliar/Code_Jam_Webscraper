#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;
const int sz=1e5+7;
double Pi;
double a[sz],b[sz],R[sz],H[sz];
int c[sz];
bool cmp(int x,int y){ return a[x]>a[y]; }
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	Pi=acos(-1);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{	int N,K,i;
		scanf("%d%d",&N,&K);
		for(i=1;i<=N;i++)
		{	scanf("%lf%lf",&R[i],&H[i]);
			a[i]=2*Pi*R[i]*H[i];
			b[i]=Pi*R[i]*R[i];
			c[i]=i;
		}
		sort(c+1,c+N+1,cmp);
		double sum=0; int d=-1;
		for(i=1;i<K;i++)
		{
			sum+=a[c[i]];
			if(d<0||R[d]<R[c[i]]) d=c[i];
		}
		double ans=sum+a[c[K]]+b[(R[d]<R[c[K]])?c[K]:d];
		for(i=K+1;i<=N;i++)
		{
			if(ans<sum+a[c[i]]+b[(R[d]<R[c[i]])?c[i]:d])
				ans=sum+a[c[i]]+b[(R[d]<R[c[i]])?c[i]:d];
		}
		printf("Case #%d: %.10f\n",casi,ans);
	}
	return 0;
}

