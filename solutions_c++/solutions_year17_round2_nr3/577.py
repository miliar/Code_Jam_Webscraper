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

ll E[128];
ll S[128];
ll G[128][128];
ll APG[128][128];
double newG[128][128];

ll dist[128];

void dij(ll s)
{
	for(int i=0;i<128;i++) dist[i] = LLONG_MAX/2;
	priority_queue<pair<ll,ll>, vector<pair<ll,ll>>, greater<pair<ll,ll>>> pq;
	pq.push(pair<ll,ll>(0, s));
	while(!pq.empty())
	{
		auto front = pq.top(); pq.pop();
		int d = front.first;
		int u = front.second;
		if(d > dist[u]) continue;
		for(ll j=0;j<128;j++)
		{
			if(G[u][j] == -1) continue;
			if(dist[u] + G[u][j] < dist[j])
			{
				dist[j] = dist[u] + G[u][j];
				pq.push(pair<ll,ll>(dist[j], j));
			}
		}
	}
}

#define INF (LLONG_MAX/2)

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		for(int i=0;i<128;i++) for(int j=0;j<128;j++) G[i][j] = INF;
		ll N,Q;
		cin>>N>>Q;
		for(ll i=0;i<N;i++) cin>>E[i]>>S[i];
		for(ll i=0;i<N;i++)
		{
			 for(ll j=0;j<N;j++) 
			 {
				 cin>>G[i][j];
				 if(G[i][j] == -1) G[i][j] = INF;
			 }
		}
		
		
		for(int i=0;i<128;i++) for(int j=0;j<128;j++) APG[i][j] = G[i][j];
		for(int k=0;k<N;k++) for(int i=0;i<N;i++) for(int j=0;j<N;j++)
		{
			if(APG[i][k] == -1 || APG[k][j] == -1) continue;
			if(APG[i][j] == -1) APG[i][j] = APG[i][k] + APG[k][j];
			else APG[i][j] = min(APG[i][j], APG[i][k] + APG[k][j]);
		}
		
//for(int i=0;i<N;i++) {for(int j=0;j<N;j++) cout<<APG[i][j]<<" ";		 cout<<"\n";}
		
		for(int i=0;i<128;i++) for(int j=0;j<128;j++) newG[i][j] = INF;
		for(int i=0;i<N;i++) for(int j=0;j<N;j++)
		{
			if(E[i] < APG[i][j]) continue;
			newG[i][j] = double(APG[i][j]) / double(S[i]);
		}
//for(int i=0;i<N;i++) {for(int j=0;j<N;j++) cout<<newG[i][j]<<" ";		 cout<<"\n";}		
		for(int k=0;k<N;k++) for(int i=0;i<N;i++) for(int j=0;j<N;j++)
		{
			if(newG[i][k] == -1 || newG[k][j] == -1) continue;
			if(newG[i][j] == -1) newG[i][j] = newG[i][k] + newG[k][j];
			else newG[i][j] = min(newG[i][j], newG[i][k] + newG[k][j]);
		}
		
		cout << "Case #" << t+1 << ":";
		for(ll i=0;i<Q;i++)
		{
			ll U,V;
			cin>>U>>V;
			cout << " " << fixed << setprecision(6) << newG[U-1][V-1];
		}
		cout << "\n";
	}
  return 0;
}
