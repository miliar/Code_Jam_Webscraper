#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	cin.ios_base::sync_with_stdio(false);
	int T,cas=1;
	cin>>T;
	while(T--)
	{
		double d;
		int n;
		cin>>d>>n;
		double mintime=-1;
		for(int i=1;i<=n;i++)
		{
			double k,v;
			cin>>k>>v;
			mintime=max(mintime,(d-k)/v);
		}
		printf("Case #%d: %.6f\n",cas++,d/mintime);
	}
}
