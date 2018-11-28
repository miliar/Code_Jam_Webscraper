#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<int,int> pii;

vector<pii> rh;
long long dp[1005][1005][2];
int visited[1005][1005][2];

long long solve (int pos, int k, int first, int n)
{
	if (!k)
		return 0;
		
	if (pos == n)
		return 0;
		
	long long &ret = dp[pos][k][first];
	
	if (!visited[pos][k][first])
	{
		long long r = rh[pos].first;
		long long h = rh[pos].second;
		
		long long area = r*r + 2LL*r*h;
		visited[pos][k][first] = true;
		ret = solve(pos+1,k,first,n);
		
		{
			long long r1 = solve(pos+1,k-1,0,n)+area;
			
			if (!first)
				r1 -= r*r;
				
			ret = max(ret,r1);
		}
	}
	
	return ret;
}

void slv ()
{
	int n,k;
	scanf("%d %d",&n,&k);
	
	rh.clear();
	for (int i = 0; i < n; i += 1)
	{
		int r,h;
		scanf("%d %d",&r,&h);
		
		rh.push_back(pii(r,h));
	}
	
	sort(rh.begin(), rh.end(),greater<pii>());
	
	memset(visited,0,sizeof visited);
	printf("%.9f\n",M_PI*solve(0,k,1,n));
}

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		printf("Case #%d: ",t);
		slv();
	}
	
	return 0;
}
