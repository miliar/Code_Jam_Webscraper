#include <bits/stdc++.h>
using namespace std;

int main()
{

freopen("hu.in","r",stdin);
  freopen("out.txt","w",stdout);
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
	string arr;
	cin>>arr;
	int k;
	cin>>k;
	int x=0;

	for(int j=0;j+k<=arr.size();j++)
	{
		if(arr[j]=='-')
		{
			for(int c=j;c<j+k;c++)
			{
				if(arr[c]=='-') arr[c]='+';
				else arr[c]='-';

			}
			x++;
		}
		//cout<<arr<<endl;
	}
int f=0;
	for(int j=0;j<arr.size();j++)
	{
		if(arr[j]=='-') f=1;
	}
	if(f==0)
	{
		cout<<"Case #"<<i<<": "<<x<<endl;
	}
	else
	{
		cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		//cout<<arr<<endl;
	}
}
}
