#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define vec vector<long long>
#define MOD 1000000007
#define ull unsigned long long
ifstream in("row10.in");
ofstream out("row10.ans");
int main()
{
	ll t,n,k,tem,i;
	in>>t;
	for(i=1;i<=t;i++)
	{
		in>>n>>k;
		priority_queue <ll> q;
		q.push(n);
		while(!q.empty())
		{
			tem=q.top();
			q.pop();
			k--;
			if(k==0)
			{
				break;
			}
			else
			{
				if(tem%2==0)
				{
					q.push((tem/2)-1);
					q.push(tem/2);
				}
				else
				{
					q.push(tem/2);
					q.push(tem/2);
				}
			}
		}
		if(tem%2==0)
		{
			out<<"Case #"<<i<<": "<<(tem/2)<<" "<<(tem/2)-1<<endl;
		}
		else
			out<<"Case #"<<i<<": "<<tem/2<<" "<<tem/2<<endl;
	}
}
