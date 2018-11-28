#include<bits/stdc++.h>
using namespace std;

#define i3 int32_t
#define i6 int64_t
#define ui3 uint32_t
#define ui6 uint64_t
#define nl nullptr
#define rt return
#define vd void
#define mp make_pair
#define th this
#define fi first
#define se second
typedef pair<i3, i3> pii;
typedef vector<i3> vi;

typedef vector<vector<pair<int,float> > > Graph;
class Comparator
{
public:
 int operator() ( const pair<int,float>& p1, const pair<int,float> &p2)
 {
 return p1.second>p2.second;
 }
};

float dijkstra(const Graph  &G,const int &source,const int &destination)
{
vector<float> d(G.size());
for(unsigned int i = 0 ;i < G.size(); i++)
{
 d[i] = std::numeric_limits<float>::max();
}
priority_queue<pair<int,float>, vector<pair<int,float> >, Comparator> Q;
d[source] = 0.0f;
Q.push(make_pair(source,d[source]));
while(!Q.empty())
{
 int u = Q.top().first;
 if(u==destination) break;
 Q.pop();
 for(unsigned int i=0; i < G[u].size(); i++)
 {
  int v= G[u][i].first;
  float w = G[u][i].second;
  if(d[v] > d[u]+w)
  {
   d[v] = d[u]+w;
   Q.push(make_pair(v,d[v]));
  }
 }
}

return d[destination];
}


vd calc()
{
	int x,y,n,q;

	cin>>n>>q;
	int dist[n],spd[n];
	for(int i=0;i<n;i++)
	{
		cin>>dist[i]>>spd[i];
	}
	int ma3x[n][n];
	Graph tmp;
	tmp.resize(n);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cin>>x;
			if(x!=-1)
			tmp[i].push_back(mp(j,x));
		}
	}
	Graph g;
	g.resize(n);
	for(int i=0;i<n;i++)
	{
		bool used[n];
		for(int i=0;i<n;i++) used[i]=0;
		stack<int> s;
		stack<int> d;
		stack<float> dists;
		s.push(i);
		d.push(dist[i]);
		dists.push(0);
		while(!s.empty())
		{
			i3 top = s.top();
			s.pop();
			i3 dop = d.top();
			d.pop();
			float distst = dists.top();
			dists.pop();
			if(used[top]) continue;
			used[top]=1;
			for(int j=0;j<tmp[top].size();j++) 
				if(used[tmp[top][j].fi]==0) {
					if(tmp[top][j].se<=dop) 
					{
						s.push(tmp[top][j].fi);
						d.push(dop-tmp[top][j].se);

						dists.push(distst + (float)tmp[top][j].se/spd[i] );
						g[i].push_back(mp(tmp[top][j].fi,distst + (float)tmp[top][j].se/spd[i]));
					}
			}
		}
	}
	for(int i=0;i<q;i++)
	{
		cin>>x>>y;
		if(i) cout<<" ";
		cout<<dijkstra(g,x-1,y-1);
	}
	
	
}

i3 main()
{
	i3 t;
	cin>>t;
	for(int ca = 1;ca<=t;ca++)
	{
		std::cout << std::fixed << std::showpoint;
		cout<<"Case #"<<ca<<": ";
		calc();
		cout<<'\n';
	}
	return 0;
}
