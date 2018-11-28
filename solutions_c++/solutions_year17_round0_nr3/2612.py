#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <functional>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

ll N, K;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{		
		cin>>N>>K;
		priority_queue<pair<ll, ll>> q;
		q.push({N, 1});		
		ll X = N;
		while(true)
		{
			auto p = q.top();
			q.pop();
			while(!q.empty() && q.top().first == p.first)
			{
				p.second += q.top().second;
				q.pop();
			}
			X = p.first;
			if(K-p.second <= 0) break;
			if(X%2!=0) q.push({X/2, 2*p.second});
			else
			{
				q.push({X/2, p.second});
				q.push({(X-1)/2, p.second});
			}
			K -= p.second;
		}
		
		ll minx = (X-1) / 2;
		ll maxx = X / 2;		
		cout << "Case #" << t+1 << ": " << maxx << " " << minx << "\n";
	}
  return 0;
}
