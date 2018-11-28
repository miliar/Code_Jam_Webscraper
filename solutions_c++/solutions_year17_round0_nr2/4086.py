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
	long long arr,brr;
	cin>>arr;
	brr=arr;
	vector<int> xxx;
	while(arr!=0)
	{
		int x=arr%10;
		xxx.push_back(x);
		arr/=10;

	}
	reverse(xxx.begin(),xxx.end());
	if(brr<10)
	{
		cout<<"Case #"<<i<<": "<<brr<<endl; continue;
	}
	for(int j=xxx.size()-1;j>0;j--)
	{
		if(xxx[j-1]>xxx[j])
		{
			xxx[j-1]-=1;
			for(int kk=j;kk<xxx.size();kk++) xxx[kk]=9;
		}

	}
	if(xxx[0]==0)
	{
		cout<<"Case #"<<i<<": ";
		for(int j=1;j<xxx.size();j++) cout<<xxx[j];
		cout<<endl;
	}
	else
	{
		cout<<"Case #"<<i<<": ";
		for(int j=0;j<xxx.size();j++) cout<<xxx[j];
		cout<<endl;
	}
}
}
