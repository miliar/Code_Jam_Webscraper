#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("qn3.txt","r",stdin);
    freopen("outputq3.txt","w",stdout);
	int t;
	cin>>t;
	priority_queue<long long int> pq;
	for(int q=1;q<=t;q++)
	{
		while(pq.size()!=0)
		{
			pq.pop();
		}
		long long int ans1,ans2,n,k;
		cin>>n>>k;
		if(n%2==0)
		{
			pq.push(n/2);
			pq.push(n/2-1);
			ans1=n/2;
			ans2=n/2-1;
		}
		else
		{
			pq.push(n/2);
			pq.push(n/2);
			ans1=n/2;
			ans2=n/2;
		}
		k--;
		int flag=0;
		while(k-- && flag==0)
		{
			int nn=pq.top();
			if(nn==1)
			{
				flag=1;
				ans1=0;
				ans2=0;
			}
			//int rindex=pq.top().second.second;
			//int lindex=pq.top().second;//.first;
			pq.pop();
			if(nn%2==0)
			{	
				pq.push(nn/2);
				pq.push(nn/2-1);
				ans1=nn/2;
				ans2=nn/2-1;		
			}
			else
			{
				pq.push(nn/2);
				pq.push(nn/2);
				ans1=nn/2;
				ans2=nn/2;
			}
		}
		cout<<"Case #"<<q<<": "<<ans1<<" "<<ans2<<endl;
	}
}
