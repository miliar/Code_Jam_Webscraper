#include<iostream>
#include <queue>
#include <map>
using namespace std;

int main()
{
	int tn;
	cin >> tn;
	for (int i = 0; i<tn; i++)
	{
		long long int n, k;
		cin >> n >> k;
		priority_queue<long long int> q;
		map<long long int, long long int> m;
		q.push(n);
		 //cout  << n << k<<endl;
		m[n] = 1;
		cout << "Case #" << i+1 << ": ";
		long long int x = n;
		if (n!=k)
		{
		while(k >= 1 && x >= 0)
		{
			x = q.top();
			q.pop();
			if (x%2 == 0)
			{
				long long int t = x/2;
				if (m.find(t-1) != m.end())
					m[t-1] = m[t-1]+m[x];
				else
				{
					m[t-1] = m[x];	
					q.push(t-1);
				}
								
				if (m.find(t) != m.end())
					m[t] = m[t]+m[x];
				else
				{
					m[t] = m[x];	
					q.push(t);
				}
			}
			else
			{
				long long int t = (x-1)/2;
				if (m.find(t)!=m.end())
				{
					m[t] = m[t]+2*m[x];
				}
				else
				{
					q.push(t);
					m[t] = 2*m[x];
				}
			}
			k = k-m[x];
			//cout << x << " " << m[x] << " " << k <<endl;
		}
		
		
		
		if   (x%2 == 0)
			cout << x/2 << " " << x/2-1 << endl;
		else
			cout << (x-1)/2 << " " << (x-1)/2 << endl;
		}
		else
		{
			cout << "0 0" <<endl;
		}
	}
}
