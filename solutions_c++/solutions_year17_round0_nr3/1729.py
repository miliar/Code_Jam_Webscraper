#include<stdio.h>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
typedef long long ll;
typedef pair<ll,ll>pii;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("l.txt","wb",stdout);
	int data;
	scanf("%d",&data);
	for(int p=1;p<=data;p++)
	{
		ll num,kai;
		scanf("%lld%lld",&num,&kai);
		map<ll,ll>ma;
		ma[num]=1;
		for(;;)
		{
			map<ll,ll>::iterator it=ma.end();
			it--;
			pii z=*it;
			ma.erase(it);
			if(kai<=z.second)
			{
				printf("Case #%d: %lld %lld\n",p,z.first/2,(z.first-1)/2);
				break;
			}
			kai-=z.second;
			ma[z.first/2]+=z.second;
			ma[(z.first-1)/2]+=z.second;
		}
	}
}