#include<iostream>
using namespace std;
#include<queue>
pair<int,int>count(int n,int k)
{
	priority_queue<int>P;
	P.push(n);
	for(int i=1;i<k;i++)
	{
		int p=P.top();P.pop();
		if(p%2==0)
		{
			if(p/2)P.push(p/2);
			if(p/2-1)P.push(p/2-1);
		}
		else
		{
			if(p/2)P.push(p/2),P.push(p/2);
		}
	}
	int p=P.top();
	pair<int,int>ans;
	ans.first=p/2;
	ans.second=p%2?p/2:p/2-1;
	return ans;
}
main()
{
	int t;cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n,k;cin>>n>>k;
		pair<int,int>p=count(n,k);
		cout<<"Case #"<<i<<": "<<p.first<<" "<<p.second<<endl;
	}
}
