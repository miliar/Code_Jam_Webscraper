#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,w=1;
	cin>>t;
	while(t--)
	{
		double n,n1,v1,k,i,max=0,ans1,ans;
		cin>>n>>k;
		for(i=0;i<k;i++)
		{
			cin>>n1>>v1;
			if(n==n1)
				continue;
			ans=(n-n1)/v1;
			if(ans>max)
				max=ans;
		}
		ans1=n/max;
		printf("Case #%d: %.6lf\n",w++,ans1);
	}
	return 0;
}
