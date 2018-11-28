/******************************************
*    AUTHOR:         CHIRAG AGARWAL       *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;

map<LL,LL> mp;

int main() 
{
	int t;
	scanf("%d",&t);
	for(int r=1;r<=t;r++)
	{
		mp.clear();
		LL n,k;
		scanf("%lld %lld",&n,&k);
		mp[n]=1;
		LL mn,mx;
		while(true)
		{
			LL val=mp.rbegin()->first;
			if(mp[val]<k)
			{
				k-=mp[val];
				LL cnt=mp[val];
				if(val%2)
				{
					mp[val/2]+=(2*cnt);
				}
				else
				{
					mp[val/2]+=cnt;
					mp[(val/2)-1]+=cnt;
				}
				mp.erase(val);
			}
			else
			{
				if(val%2)
				{
					mn=val/2;
					mx=val/2;
				}
				else
				{
					mx=val/2;
					mn=(val/2)-1;
				}
				break;
			}
		}
		printf("Case #%d: %lld %lld\n",r,mx,mn);
	}	
	return 0;
}