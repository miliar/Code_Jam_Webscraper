#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <fstream>
#include <iterator>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)
typedef long long ll;

const ll INF=1000000000LL*1000000000LL;
const int MAXN=1000000;

struct Solver
{
	string solve(int b, int y, int r)
	{
		int n=r+y+b;
		string res(n,'-');
		priority_queue<pair<int,char> > q;
		q.push(make_pair(r,'R'));
		q.push(make_pair(y,'Y'));
		q.push(make_pair(b,'B'));
		int val;
		char sym;
		val=q.top().first;
		sym=q.top().second;
		q.pop();
		for(int i=0;i<n;i++)
			if(res[i]=='-')
			{
				for(int j=i;res[j]=='-';j=(j+2)%n)
				{
					res[j]=sym;
					val--;
					if(val==0 && !q.empty())
					{
						val=q.top().first;
						sym=q.top().second;
						q.pop();
					}
				}
			}
		return res;
	}
	string solve()
	{
		ostringstream out;
		int n,q;
		vector<int> e;
		vector<int> s;
		vector<vector<ll> > d;
		vector<vector<double> > res;
		cin>>n>>q;
		e.resize(n);
		s.resize(n);
		d.resize(n, vector<ll>(n));
		res.resize(n, vector<double>(n));
		REP(i,n)
			cin>>e[i]>>s[i];
		REP(i,n)
			REP(j,n)
			{
				cin>>d[i][j];
				if(d[i][j]==-1)
					d[i][j]=INF;
			}
		REP(i,n)
			d[i][i]=0;
		REP(k,n)
			REP(i,n)
				REP(j,n)
					d[i][j]=min(d[i][j], d[i][k]+d[k][j]);
		REP(i,n) REP(j,n)
			if(d[i][j]<=e[i])
				res[i][j]=double(d[i][j])/s[i];
			else
				res[i][j]=1e100;
		REP(k,n)
			REP(i,n)
				REP(j,n)
					res[i][j]=min(res[i][j], res[i][k]+res[k][j]);
		out<<fixed<<setprecision(10);
		REP(i,q)
		{
			int u,v;
			cin>>u>>v;
			u--;
			v--;
			if(i)
				out<<" ";
			out<<res[u][v];
		}
		out<<endl;

		return out.str();
	}
};

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
		printf("Case #%d: %s",test, Solver().solve().c_str());
	return 0;
}
