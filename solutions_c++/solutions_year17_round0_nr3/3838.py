#include <bits/stdc++.h>
#define ll long long 
#define m 1000000007
using namespace std;
priority_queue<ll>pq;
int main() {
	// your code goes here
	std::ios::sync_with_stdio(false);
	ll t,n,k,al,ah,y=1;
	cin>>t;
	while(t--)
	{ 
		ll c=0;
		cin>>n>>k;
		pq.push(n);
		while(!pq.empty() && c!=k)
		{
			ll x=pq.top();
			pq.pop();
			if(x%2)
			{
				pq.push(x/2);
				pq.push(x/2);
				al=min(x/2,x/2);
				ah=max(x/2,x/2);
			}
			else
			{
				pq.push(x/2);
				pq.push(x/2-1);
				al=min(x/2-1,x/2);
				ah=max(x/2-1,x/2);
			}
			c++;
		}
		cout<<"Case #"<<y<<": ";
		cout<<ah<<" "<<al<<endl;
		y++;
		while(!pq.empty())
		pq.pop();
	}
	

	
	return 0;
}
