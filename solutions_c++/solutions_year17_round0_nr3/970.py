#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
long long n,k,minn,maxx,cminn,cmaxx;
int test;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("q3.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		printf("Case #%d: ",kk);
		cin>>n>>k;
		long long now=1;
		minn=(n-1)/2;
		maxx=n-1-minn;
		if (k==1) 
		{
			printf("%lld %lld\n",maxx,minn);
			continue;
		}
		cmaxx=cminn=1;
		while (now*2+1<k)
		{
			now=now*2+1;
			if (minn==1)
			{
				cminn=0;
				minn=0;
				maxx=1;
			}
			else if (minn==2)
			{
				if (maxx>2)
				{
					cmaxx=cminn+cmaxx*2;
				}
				else
				{
					cmaxx+=cminn;
					cminn=cmaxx;
				}
				maxx=1;
				minn=0;
			}
			else if (minn&1)
			{
				cminn=2*cminn+cmaxx;
				minn=(minn-1)/2;
				maxx=maxx-1-minn;
			}
			else
			{
				if (minn==maxx)
				{
					cminn+=cmaxx;
					cmaxx=cminn;
				}
				else
				{
					cmaxx=cmaxx*2+cminn;
				}
				minn=(minn-1)/2;
				maxx=minn+1;
			}
	//		cout<<maxx<<' '<<cmaxx<<' '<<minn<<' '<<cminn<<endl;
		}
		k-=now;
//		cout<<cmaxx<<cminn<<endl;
		if (k<=cmaxx) printf("%lld %lld\n",maxx-(maxx-1)/2-1,(maxx-1)/2);
		else printf("%lld %lld\n",minn-(minn-1)/2-1,(minn-1)/2);
	}
	return 0;
}
