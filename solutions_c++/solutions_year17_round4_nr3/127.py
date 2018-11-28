#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <cassert>
using namespace std;

const int INF=2000000000;

typedef long long ll;

int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};

class TwoSat
{
	int n;
	vector<vector<int> >v, vt;
	vector<int> used, order, comp;
	void dfs(int cur)
	{
		if(used[cur]) return;
		used[cur]=true;
		for(int i=0;i<v[cur].size();i++)
		{
			dfs(v[cur][i]);
		}
		order.push_back(cur);
	}

	void color(int cur, int clr)
	{
		if(comp[cur]!=-1) return;
		comp[cur]=clr;
		for(int i=0;i<vt[cur].size();i++)
			color(vt[cur][i], clr);
	}
public:
	int neg(int x)
	{
	    return x^1;
	}

	int var(int x)
	{
	    return x*2;
	}

	void add_term(int x1, int x2)
	{
	    v[neg(x1)].push_back(x2);
	    v[neg(x2)].push_back(x1);
	    vt[x2].push_back(neg(x1));
	    vt[x1].push_back(neg(x2));
	}

	TwoSat(int n):
		n(n)
	{
		v.resize(2*n);
		vt.resize(2*n);
		used.resize(2*n);
		comp.resize(2*n);
	}

	vector<int> solve()
	{
		fill(used.begin(), used.end(), 0);
		fill(comp.begin(), comp.end(), -1);
		for(int i=0;i<2*n;i++)
		{
			if(!used[i])
				dfs(i);
		}
		int top=0;
		while(!order.empty())
		{
			int cur=order.back(); order.pop_back();
			if(comp[cur]==-1)
				color(cur, top++);
		}

		for(int i=0;i<n;i++)
			if(comp[var(i)]==comp[neg(var(i))])
				return vector<int>();
		vector<int> res(n);
		for(int i=0;i<n;i++)
			res[i]=comp[var(i)]>comp[neg(var(i))];
		return res;
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
	int interact(int dir, char c)
	{
		switch(c)
		{
		case '|':
		case '-':
		case '#':
			return -1;
		case '/':
			return dir^1;
		case '\\':
			return dir^3;
		case '.':
			return dir;
		default:
			throw;
		}
	}
	vector<string> f;
	vector<pair<int,int> > mirrors;
	vector<vector<int> > beam[2];
	void solve(ostringstream& out)
	{
			int r,c;
			cin>>r>>c;
			f.resize(r);
			for(int i=0;i<r;i++)
				cin>>f[i];
			beam[0].resize(r,vector<int>(c,-1));
			beam[1].resize(r,vector<int>(c,-1));


			for(int i=0;i<r;i++)
				for(int j=0;j<c;j++)
					if(f[i][j]=='|' || f[i][j]=='-')
						mirrors.emplace_back(i,j);

			TwoSat sat((int)mirrors.size());
			//vertical - 0
			//horizontal - 1

			for(int k=0;k<mirrors.size();k++)
			{
				int i=mirrors[k].first;
				int j=mirrors[k].second;
				if(f[i][j]=='|' || f[i][j]=='-')
				{
					for(int dir=0;dir<4;dir++)
					{
						int x=i+dx[dir];
						int y=j+dy[dir];
						int cd=dir;
						int var;
						if(dir%2==0)
							var=sat.neg(sat.var(k));
						else
							var=sat.var(k);
						while(0<=x && x<r && 0<=y && y<c)
						{
							if(f[x][y]=='.')
								beam[cd%2][x][y]=var;
							cd=interact(cd, f[x][y]);
							if(cd<0) break;
							x+=dx[cd];
							y+=dy[cd];
						}
						if(0<=x && x<r && 0<=y && y<c && (f[x][y]=='|' || f[x][y]=='-'))
						{
							//forbid
							sat.add_term(sat.neg(var), sat.neg(var));
						}
					}
				}
			}
			bool ok=true;
			for(int i=0;i<r && ok;i++)
				for(int j=0;j<c && ok;j++)
					if(f[i][j]=='.')
					{
						if(beam[0][i][j]==-1 && beam[1][i][j]==-1)
							ok=false;
						else if(beam[0][i][j]==-1)
							sat.add_term(beam[1][i][j], beam[1][i][j]);
						else if(beam[1][i][j]==-1)
							sat.add_term(beam[0][i][j], beam[0][i][j]);
						else
							sat.add_term(beam[0][i][j], beam[1][i][j]);
					}
			vector<int> res;
			if(ok)
			{
				res=sat.solve();
				ok&=!res.empty();
			}

			if(ok)
			{
				for(int i=0;i<(int)mirrors.size();i++)
				{
					if(res[i]==0)
						f[mirrors[i].first][mirrors[i].second]='|';
					else
						f[mirrors[i].first][mirrors[i].second]='-';
				}
			}

			if(!ok)
				out<<"IMPOSSIBLE"<<endl;
			else
			{
				out<<"POSSIBLE"<<endl;
				for(int i=0;i<r;i++)
					out<<f[i]<<endl;
			}
	}
};

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
		printf("Case #%d: %s",test,Solver().solve().c_str());
	return 0;
}
