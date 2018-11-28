#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;
const int sz=1e5+7;
struct SEG
{	int l,r,k;
	SEG(int a=0,int b=0,int c=0):l(a),r(b),k(c){};
}a[sz],b[sz]; int bn=0;
bool cmp(SEG u,SEG v){ return u.l<v.l; }
bool cmp2(SEG u,SEG v){ return (u.r-u.l)<(v.r-v.l); }
int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{
		int C,J,i; cin>>C>>J; int sum[5]; sum[1]=sum[2]=720;
		for(i=1;i<=C;i++)
		{
			scanf("%d%d",&a[i].l,&a[i].r); a[i].k=2; sum[2]-=a[i].r-a[i].l;
		}
		for(i=C+1;i<=C+J;i++)
		{
			scanf("%d%d",&a[i].l,&a[i].r); a[i].k=1; sum[1]-=a[i].r-a[i].l;
		}
		sort(a+1,a+C+J+1,cmp);
		int ans=0;
		bn=0;
		for(i=2;i<=C+J;i++) if(a[i-1].k==a[i].k)
		{
			if(a[i].l-a[i-1].r>0){b[++bn]=SEG(a[i-1].r,a[i].l,a[i].k); ans+=2;}
			//else if(a[i].l-a[i-1].r<0) printf("ERROR_1!_%d_%d\n",a[i].l,a[i-1].r);
		}
		else ans++;
		if(a[C+J].k==a[1].k)
		{
			if(a[1].l+1440-a[C+J].r>0){b[++bn]=SEG(a[C+J].r,a[1].l+1440,a[1].k); ans+=2;}
			//else if(a[1].l+1440-a[C+J].r<0)printf("ERROR_2!\n");
		}
		else ans++;
		//printf("ANS1=%d\n",ans);
		sort(b+1,b+bn+1,cmp2);
		for(i=1;i<=bn;i++) if(sum[b[i].k]>=b[i].r-b[i].l)
		{
			//printf("(%d,%d)_%d\n",b[i].l,b[i].r,b[i].k);
			sum[b[i].k]-=b[i].r-b[i].l;
			ans-=2;
		}
		printf("Case #%d: %d\n",casi,ans);
	} 
	return 0;
}

