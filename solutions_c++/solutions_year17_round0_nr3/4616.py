#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define max 100010
char a[max];
char ans[max];
priority_queue<ll> pq;
int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("ans6.txt","w",stdout);
	ll t;
	cin>>t;
	ll  kase=1;
	while(t--)
	{
		ll n,k;
		cin>>n>>k;
		while(!pq.empty())
		pq.pop();
		pq.push(n);
		ll m=k-1;
		while(m--)
		{
			ll p=pq.top();
			pq.pop();
			if(p%2==1)
			{
				pq.push(p/2);
				pq.push(p/2);
			}
			else
			{
				pq.push(p/2);
				pq.push((p/2)-1);
			}
		}
		ll k1,k2;
		ll kk=pq.top();
		if(kk%2==1)
		{
			k1=kk/2;
		   k2=kk/2;
		}
		else
		{
			k1=kk/2;
			k2=kk/2-1;
		}
		
			cout<<"Case #"<<kase<<": "<<k1<<" "<<k2<<endl;
		kase++;
	}
}
