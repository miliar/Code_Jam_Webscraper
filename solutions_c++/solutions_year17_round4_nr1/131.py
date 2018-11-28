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

struct Solver
{
	string solve()
	{
		ostringstream out;
		solve(out);
		return out.str();
	}
	map<vector<int>, int> dp;
	int solve(int left, int rem, int p, vector<int> cnt)
	{
		if(left==0) return 0;
		if(!dp.count(cnt))
		{
			int res=0;
			for(int i=1;i<(int)cnt.size();i++)
				if(cnt[i])
				{
					cnt[i]--;
					res=max(res, solve(left-1, (rem+i)%p, p, cnt));
					cnt[i]++;
				}
			dp[cnt]=(rem%p==0)+res;
		}
		return dp[cnt];
	}
	void solve(ostringstream& out)
	{
		int n,p;
		cin>>n>>p;
		vector<int> g(n);
		vector<int> cnt(p);
		for(int i=0;i<n;i++)
			cin>>g[i];
		for(int i=0;i<n;i++)
			cnt[g[i]%p]++;
		int res=cnt[0]+solve(n-cnt[0], 0, p, cnt);
		out<<res<<endl;
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
