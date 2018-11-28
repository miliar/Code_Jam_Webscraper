#include<bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
int main()
{
	ll T, n, k;
	ll t=1;
	cin>>T;
	while(t<=T)
	{
		cin>>n>>k;
		ll mn = ll(1e18), mx = 0;
		priority_queue<ll> pq;
		pq.push(n);
		while(k--)
		{
			ll ele = pq.top();
			pq.pop();
			if(ele&1)
			{
				//if(ele/2!=0)
				//{
					pq.push(ele/2);pq.push(ele/2);
					mn = ele/2; mx = ele/2;
				//}
			}
			else
			{
				//if(ele/2!=0)
				//{
					pq.push(ele/2-1);pq.push(ele/2);
					mn = ele/2-1; mx = ele/2;
				//}	
			}
		}
		cout<<"Case #"<<t<<": "<<mx<<" "<<mn<<endl;
		++t;
	}
	return 0;
}