#include<iostream>
#include<cstdio>

using namespace std;

int T;
long long n,k;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	scanf("%d",&T);
	for (int cas=1;cas<=T;++cas) 
	{
		scanf("%lld%lld",&n,&k);
		long long X=n,Y=n+1;
		long long x=1,y=0;
		printf("Case #%d: ",cas);
		while (true)
		{
		//	cout<<X<<' '<<Y<<' '<<x<<' '<<y<<' '<<k<<endl;
			if (y>=k)
			{
				printf("%lld %lld\n",Y-1-(Y-1)/2,(Y-1)/2);
				break;
			}
			else k-=y;
			if (x>=k)
			{
				printf("%lld %lld\n",X-1-(X-1)/2,(X-1)/2);
				break;
			}
			else k-=x;
			long long xx=x;
			long long yy=y;
			if (X&1) xx+=x;
			else yy+=x;
			if (Y&1) yy+=y;
			else xx+=y;
			x=xx;
			y=yy;
			X=(X-1)/2;
			Y=Y/2;
		} 
	}
	return 0;
} 
