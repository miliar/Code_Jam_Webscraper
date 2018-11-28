#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	int t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		priority_queue<int> q;
		int n,k,i;
		cin>>n>>k;
		for(i=1;i<k;i++)
		{
			if(n%2==0)
			{
				q.push((n-1)/2);
				q.push(n/2);
			}
			else
			{
				q.push(n/2);
				q.push(n/2);
			}
			n=q.top();
			q.pop();
		}
		if(n%2==0)
		cout<<"Case #"<<j<<": "<<n/2<<" "<<(n-1)/2<<endl;
		
		else
		cout<<"Case #"<<j<<": "<<n/2<<" "<<(n)/2<<endl;
		
	}
	return 0;
}
