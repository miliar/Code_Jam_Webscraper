#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <sstream>
#include <cassert>
using namespace std;

const int INF=2000000000;

typedef long long ll;

int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};

class MincostMaxflow
{
	int n;
	vector<int> hd;
	vector<int> to, nxt, cap, cost;
public:
	MincostMaxflow(int n):
		n(n),
		hd(n,-1),
		phi(n,0)
	{
	}
	int get_n() const
	{
		return n;
	}
	/*
	 * add edge from a to b with capacity cp and cost cs
	 * returns id of created edge
	 */
	int add_edge(int a, int b, int cp, int cs)
	{
		assert(0<=a && a<n);
		assert(0<=b && b<n);
		int res=to.size();
		int ecnt=to.size();

		to.push_back(b);
		nxt.push_back(hd[a]);
		cap.push_back(cp);
		cost.push_back(cs);
		hd[a]=ecnt;
		ecnt++;

		to.push_back(a);
		nxt.push_back(hd[b]);
		cap.push_back(0);
		cost.push_back(-cs);
		hd[b]=ecnt;
		ecnt++;

		return res;
	}
	int get_to(int edge)
	{
		return to[edge];
	}
	int get_from(int edge)
	{
		return to[edge^1];
	}
	void increase_cost(int edge, int val)
	{
		cost[edge]+=val;
		cost[edge^1]-=val;
	}
	/*
	 * find path with minimal cost from s to t
	 */
	vector<int> phi;
	vector<int> find_path(int s, int t, bool bfs=false)
	{
		vector<int> res;
		vector<int> dist(n,INF);
		vector<int> prv(n,-1);
		priority_queue<pair<int,int>, vector<pair<int,int> >, greater<pair<int,int> > > q;
		dist[s]=0;
		q.push(make_pair(dist[s],s));
		while(!q.empty())
		{
			int cur=q.top().second;
			int curd=q.top().first;
			q.pop();
			if(dist[cur]!=curd) continue;
			for(int i=hd[cur];i!=-1;i=nxt[i])
			{
				int nd=curd+(bfs?1:(cost[i]-phi[to[i]]+phi[cur]));
				assert(cap[i]==0 || nd-curd>=0);
				if(cap[i]>0 && dist[to[i]]>nd)
				{

					dist[to[i]]=nd;
					prv[to[i]]=i;
					q.push(make_pair(dist[to[i]], to[i]));
				}
			}
		}
		if(!bfs)
			for(int i=0;i<n;i++)
				if(dist[i]!=INF)
					phi[i]+=dist[i];
		if(dist[t]!=INF)
		{
			int cur=t;
			while(cur!=s)
			{
				res.push_back(prv[cur]);
				cur=to[prv[cur]^1];
			}
			reverse(res.begin(), res.end());
		}
		return res;
	}
	/*
	 * find minimal cost maximal flow from s to t and change graph accordingly
	 * returns pair(flow, cost)
	 */
	pair<int,int> find_flow(int s, int t)
	{
		int flow=0;
		int cst=0;
		vector<int> path;
		while(!(path=find_path(s,t)).empty())
		{
			int min_cap=INF;
			for(int i:path)
				min_cap=min(min_cap, cap[i]);
			flow+=min_cap;
			for(int i:path)
			{
				cst+=min_cap*cost[i];
				cap[i]-=min_cap;
				cap[i^1]+=min_cap;
			}
		}
		return make_pair(flow, cst);
	}
	/*
	 * decompose flow into paths from s to t
	 * returns vector of paths, each of which is a set of edges, and their quantity
	 */
	vector<pair<vector<int>,int> > extract_paths(int s, int t)
	{
		vector<int> cap_tmp=cap;
		for(size_t i=0;i<cap.size();i+=2)
			cap[i]=0;
		vector<pair<vector<int>, int> > res;
		vector<int> path;
		while(!(path=find_path(t,s,true)).empty())
		{
			int min_cap=INF;
			for(int i:path)
				min_cap=min(min_cap, cap[i]);
			for(int &i:path)
			{
				cap[i]-=min_cap;
				cap[i^1]+=min_cap;
				i^=1;
			}
			reverse(path.begin(), path.end());
			res.push_back(make_pair(path, min_cap));
		}
		cap=cap_tmp;
		return res;
	}
	void reset()
	{
		for(size_t i=0;i<cap.size();i+=2)
		{
			cap[i]+=cap[i^1];
			cap[i^1]=0;
		}
		fill(phi.begin(), phi.end(),0);
	}
};

struct Solver
{
	string solve()
	{
		ostringstream out;
		solve(out);
		return out.str();
	}

	void solve(ostringstream& out)
	{
			int n,c,m;
			scanf("%d%d%d",&n,&c,&m);
			assert(c==2);
			vector<int> t[2];
			for(int i=0;i<m;i++)
			{
				int p,b;
				scanf("%d%d",&p,&b);
				b--;
				t[b].push_back(p);
			}
			int n1=t[0].size();
			int n2=t[1].size();
			MincostMaxflow flow(n1+n2+2);
			int source=flow.get_n()-2;
			int sink=flow.get_n()-1;
			for(int i=0;i<n1;i++)
				flow.add_edge(source, i, 1, 0);
			for(int i=0;i<n1;i++)
				for(int j=0;j<n2;j++)
					if(t[0][i]!=t[1][j])
						flow.add_edge(i,n1+j, 1, 0);
					else if(t[0][i]!=1)
						flow.add_edge(i,n1+j, 1, 1);
			for(int i=0;i<n2;i++)
				flow.add_edge(n1+i, sink, 1, 0);
			pair<int,int> res=flow.find_flow(source, sink);
			out<<n1+n2-res.first<<" "<<res.second<<endl;
	}
};

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		cerr<<test<<endl;
		printf("Case #%d: %s",test,Solver().solve().c_str());
	}
	return 0;
}
