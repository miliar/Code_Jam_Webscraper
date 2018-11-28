/******************************************
*    AUTHOR:         CHIRAG AGARWAL       *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;

int n,k;
pair<long long, long long> help[1003];
const double PI=3.14159265359;	
long long arr[1003];

int main() 
{
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		scanf("%d %d",&n,&k);
		for(int i=1;i<=n;i++)
		{
			scanf("%lld %lld",&help[i].first,&help[i].second);
		}
		sort(help+1,help+n+1);
		long long ans=0;
		for(int i=k;i<=n;i++)
		{	
			long long temp=((help[i].first)*(help[i].first))+(2*help[i].first*help[i].second);
			int cur=0;
			for(int l=i-1;l>=1;l--)
			{
				arr[cur]=help[l].first*help[l].second*2;
				cur++;
			}
			sort(arr,arr+cur);
			for(int l=cur-1;l>=cur-k+1;l--)
			{	
				temp+=arr[l];
			}
			ans=max(ans,temp);
		}
		printf("Case #%d: %lf\n",tc,ans*PI);
	}	
	return 0;
}