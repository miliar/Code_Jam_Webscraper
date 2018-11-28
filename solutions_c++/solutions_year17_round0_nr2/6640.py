#include<bits/stdc++.h>
using namespace std;
string a;
int flag[50];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output_large.txt","w",stdout);
	int i,j,t,cas=0,f=0,n;
	cin>>t;
	while(t--)
	{
		memset(flag,0,sizeof(flag));
		cin>>a;
		n=a.length();
		for(i=n-2;i>=0;i--)
		{
			if(a[i]>a[i+1])
			{
				a[i]--;
				a[i+1]='9';
				flag[i+1]=1;
			}
		}
		
		for(i=1;i<n;i++)
		{
			if(flag[i])
			{
				for(j=i+1;j<n;j++)
				{
					a[j]='9';
				}
				break;
			}
		}
		cout<<"Case #"<<++cas<<": ";
		f=0;
		for(i=0;i<n;i++)
		{
			if(!f && a[i]=='0')
			continue;
			else
			{
				cout<<a[i];
				f=1;
			}
		}
		cout<<endl;
	}
	return 0;
}
	
