#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
int main()
{
	int t,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		int n,i,r,o,y,g,b,v;
		int mxm=0,ar;
		pair<int,char> p[6];
		string s="ROYGBV";
		cin>>n;
		for(i=0;i<6;i++)
		{

			cin>>ar;
			p[i].first=ar;
			p[i].second=s[i];
			mxm=max(mxm,ar);
		}
		sort(p,p+6);
		printf("Case #%d: ",z);
		if(mxm>n/2)
			cout<<"IMPOSSIBLE\n";
		else
		{
			int j=0,k=5;
			char arr[1005];
			for(i=0;i<n;i++)
			{
				while(p[k].first)
				{
					arr[j]=p[k].second;
					p[k].first--;
					j+=2;
					if(j>=n)
						j=1;
				}
				k--;
				if(k<0)
					break;
			}
			for(i=0;i<n;i++)
				printf("%c",arr[i]);
			printf("\n");
		}


	}
	return 0;
}