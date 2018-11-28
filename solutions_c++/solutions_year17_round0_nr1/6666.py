#include<bits/stdc++.h>
using namespace std;
string a;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output_large.txt","w",stdout);
	int i,j,k,l,m,n,t,cnt=0,cas=0;
	cin>>t;
	while(t--)
	{
		cin>>a;
		cin>>k;
		cnt=0;
		n=a.length();
		for(i=0;i<n;i++)
		{
			if(a[i]=='+')
			continue;
			else
			{
				if(i+k>n)
				break;
				
				for(j=0;j<k;j++)
				{
					if(a[i+j]=='+')
					a[i+j]='-';
					else
					a[i+j]='+';
				}
				cnt++;
			}
		}
		cout<<"Case #"<<++cas<<": ";
		if(i==n)
		cout<<cnt;
		else
		cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}
