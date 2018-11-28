//suryaveer
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
	freopen("c_in.in","r",stdin);
	freopen("c_out.out","w",stdout);
	ll t;
	ll n,k,tog;
	cin>>t;
	for(ll i=1;i<=t;i++)
	{
		cin>>n>>k;
		priority_queue<ll>que;

		que.push(n);
		for(ll j=1;j<=k;j++)
		{
			tog=que.top();
			que.pop();
			que.push((tog-1)/2);
			que.push(tog/2);	
			
			if(j==k){
				cout<<"Case #"<<i<<": "<<max(tog/2,(tog-1)/2)<<" ";
				cout<<min(tog/2,(tog-1)/2)<<endl;
			}
		}
	}
	return 0;	
}