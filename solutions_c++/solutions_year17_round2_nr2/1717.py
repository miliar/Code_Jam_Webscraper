#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;

int main()
{
	int t;
	int n,r,o,y,g,b,v;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("newoutput4.out","w",stdout);
	scanf("%d",&t);
	for(int k=1; k<=t; k++)
	{
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		vector< pair<int,char> > v(3);
		v[0]=make_pair(r,'R');
		v[1]=make_pair(y,'Y');
		v[2]=make_pair(b,'B');
		sort(v.rbegin(),v.rend());
		printf("Case #%d: ",k);
		if(v[0].first>v[1].first+v[2].first)
		printf("IMPOSSIBLE");
		else
		{
		int x = v[0].first - v[1].first;
		int i;
		for(i=0;i<x;i++)
		printf("%c%c%c%c",v[0].second,v[1].second,v[0].second,v[2].second);
		for(;i<v[2].first;i++)
		printf("%c%c%c",v[0].second,v[1].second,v[2].second);
		for(;i<v[1].first;i++)
		printf("%c%c",v[0].second,v[1].second);
		}
		printf("\n");
	}
	return 0;
}
