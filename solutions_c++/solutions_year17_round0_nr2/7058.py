#include<bits/stdc++.h>
using namespace::std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		char n[20];
		cin>>n;
		int l=strlen(n);
		for(int i=l-1;i>0;i--)
		{
			if(n[i]<n[i-1])
			{
				for(int j=i;j<l;j++)
					n[j]='9';
				n[i-1]=n[i-1]-1;
			}
		}
		int f=0;
		//unsigned long long int res;
		//res = ull(n);
		for(int i=0;i<l;i++)
			{if(n[i]!='0')
			{
				f=i;
				break;
			}}
		cout<<"Case #"<<c<<": ";
		for(int i=f;i<l;i++)
			cout<<n[i];
		cout<<endl;
	}
	return 0;
}
