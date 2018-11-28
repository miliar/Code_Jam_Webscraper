#include <stdio.h>
#include <map>
std::map<long long,long long> mymap;
std::map<long long,long long>::iterator iter;
void doe()
{
	long long n,k,kid,gogo;
	mymap.clear();
	scanf("%lld %lld",&n,&k);
	k--;
	mymap[n]=1;
	while(1)
	{
		iter=(--mymap.end());
		if(iter->second>k)
		{
			gogo=iter->first;
			break;
		}
		k-=iter->second;
		kid=iter->first;
		if(kid%2==0)
		{
			if(mymap.find(kid/2)==mymap.end())
				mymap[kid/2]=iter->second;
			else
				mymap[kid/2]+=iter->second;
			if(mymap.find(kid/2-1)==mymap.end())
				mymap[kid/2-1]=iter->second;
			else
				mymap[kid/2-1]+=iter->second;
		}
		else
		{
			if(mymap.find(kid/2)==mymap.end())
				mymap[kid/2]=2*iter->second;
			else
				mymap[kid/2]+=2*iter->second;
		}
		mymap.erase(iter);
	}
	if(gogo%2==1)
	{
		printf("%lld %lld\n",gogo/2,gogo/2);
	}
	else
	{
		printf("%lld %lld\n",gogo/2,gogo/2-1);
	}
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		doe();
	}
	return 0;
}