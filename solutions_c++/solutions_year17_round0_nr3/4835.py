#include <bits/stdc++.h>
using namespace std;
int main (void)
{
	int t;
	cin>>t;
	for(int x = 1 ; x <= t ; x++)
	{
		long long n,k;
		cin>>n>>k;
		priority_queue<long long> pq;
		pq.push(n);
		k--;
		while(k--)
		{
			int value = pq.top();
			pq.pop();
			if(value & 1)
			{
				pq.push((value-1)/2);
				pq.push((value-1)/2);
			}
			else
			{
				pq.push(value/2);
				pq.push((value/2)-1);
			}
		}
		int sol1,sol2;
		int ans1 = pq.top();
		pq.pop();
		if(ans1 & 1)
		{
			sol1 = (ans1-1)/2;
			sol2 = (ans1-1)/2;
		}
		else
		{
			sol1 = ans1/2;
			sol2 = (ans1/2)-1;
		}
		printf("Case #%d: ",x);
		cout<<sol1<<" "<<sol2<<endl;
	}
}