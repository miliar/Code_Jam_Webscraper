#include <bits/stdc++.h>

using namespace std;

map<long long,long long> q;
long long t,n,k,ans;

int main()
{
	scanf("%lld",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%lld%lld",&n,&k);
		q.clear();
		q[n]=1;
		while( !q.empty() )
		{
			long long temp =(*q.rbegin()).first;
			long long d =(*q.rbegin()).second;
			
			if( temp%2 == 1 )
			{//ganjil
				q[temp/2] += d*2;
			}else
			{//genap
				q[temp/2] +=d;
				q[temp/2 -1 ] +=d;
			}	
			k=k-d;
			if(k<=0)
			{
				ans=temp;
				break;
			}
			
			q.erase(temp);
		}
		printf("Case #%d: ",i);
		if(ans%2 == 1)
			printf("%lld %lld\n",ans/2,ans/2);
		else
			printf("%lld %lld\n",ans/2,ans/2-1);
	}
	
	return 0;
}
