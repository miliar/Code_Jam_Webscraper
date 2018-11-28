#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <utility>
#include <cstring>
#include <cstdio>
using namespace std;
typedef long long int ll;
double pi = 3.1415926535897932;
int main()
{
	ios::sync_with_stdio(false);
	ll t, n, k, r[1000], h[1000], area1[1000], area2[1000];	
	cin>>t;
	for (int z = 0; z < t; z++)
	{
		cin>>n>>k;
		for (int i = 0; i < n; i++)
		{
			cin>>r[i]>>h[i];
			area1[i] = r[i]*r[i];
			area2[i] = r[i]*h[i]*2;
		}
		priority_queue<pair<ll, int> > q, q1;
		for (int i = 0; i < n; i++)
		{
			q.push(make_pair(area2[i], i));
		}
		ll sum = 0, minim = 1e18, rmax = 0, count = 0, ans = 0;
		while (!q.empty())
		{
			pair<ll, int> temp = q.top(); q.pop(); 
			if (count < k)
			{
				sum += temp.first;
				minim = min(minim, temp.first);
				rmax = max(rmax, area1[temp.second]);
				count++;
			}
			else
			{
				sum -= minim;
				minim = temp.first;
				sum += temp.first;
				rmax = max(rmax, area1[temp.second]);
				count++;
			}
			ans = max(ans, sum+rmax);
		}
		double ans1 = pi*double(ans);
		cout<<"Case #"<<z+1<<": ";
		printf("%.7F", ans1);
		cout<<"\n";
	}
}