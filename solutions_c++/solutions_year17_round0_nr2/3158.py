#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;

int main()
{
	int t,i,j,size;
	lli n;
	freopen("B-large (1).in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	vector<int> v;
	vector<int>::iterator itt;
	for(int testcase=1; testcase<=t; testcase++)
	{
		scanf("%lld",&n);
		printf("Case #%d: ",testcase);
		while(n)
		{
			v.push_back(n%10);
			n/=10;
		}
		reverse(v.begin(),v.end());
		size=v.size();
		i=1;
		while(i<size && v[i]>=v[i-1])
		i++;
		if(i==size)
		{
			for(i=0;i<size;i++)
			printf("%d",v[i]);
		}
		else
		{
			j=i;
			for(;j<size;j++)
			v[j]=9;
			i--;
			while(i>0 && v[i]==v[i-1])
			{
				v[i]=9;
				i--;
			}
			v[i]--;
			for(i=0;i<size;i++)
			if(v[i])
			printf("%d",v[i]);
		}
		printf("\n");
		v.clear();
	}
	return 0;
}
