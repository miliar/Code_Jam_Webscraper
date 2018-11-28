#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,l,fl;
	string n;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		fl=0;
		cin>>n;
		l=n.length();
		for(int j=l-1;j>0;j--)
		{
			if(n[j]<n[j-1])
			{
				n[j]='9';
				n[j-1]--;
			}
		}
		for(int j=1;j<l;j++)
		{
			if(n[j-1]=='9')
			{
				n[j]='9';
			}
		}
		printf("Case #%d: ",i);
		for(int j=0;j<l;j++)
		{
			if(n[j]!='0')
				fl=1;
			if(fl==1)
				cout<<n[j];
		}
		cout<<'\n';
	}
	return 0;
}