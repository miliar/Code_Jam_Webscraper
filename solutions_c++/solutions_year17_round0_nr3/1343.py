#include <iostream>
#include <map>
#include <queue>
using namespace std;
typedef long long int ll;
int main()
{
	ll t, k, n, a1, a2;
	cin>>t;
	for (int y = 0; y < t; y++)
	{
		cin>>n>>k;
		ll temp = 0, plus = 1;
		a1 = a2 = 0;
		priority_queue<ll> pq;
		pq.push(n);
		map<ll, ll> m;
		m[n] = 1;
		while (temp < k)
		{
			ll temp1 = pq.top(), temp2; pq.pop();
			temp2 = m[temp1];
			m[temp1] = 0;
			temp += temp2;
			if (temp1 % 2 == 0)
			{
				a1 = temp1/2;
				a2 = a1-1;
				if (m.count(a1) > 0 and m[a1] != 0)
				{
					m[a1] += temp2;
				}
				else
				{
					pq.push(a1);
					m[a1] = temp2;
				}

				if (m.count(a2) > 0 and m[a2] != 0)
				{
					m[a2] += temp2;
				}
				else
				{
					pq.push(a2);
					m[a2] = temp2;
				}
			} 
			else
			{
				a1 = a2 = temp1/2;
				if (m.count(a1) > 0 and m[a1] != 0)
				{
					m[a1] += 2*temp2;
				}
				else
				{
					pq.push(a1);
					m[a1] += 2*temp2;
				}
			}
		}
		cout<<"Case #"<<y+1<<": ";
		cout<<a1<<" "<<a2<<"\n";
	}
}