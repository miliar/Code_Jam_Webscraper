#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
#define EPS 10E-8
using namespace std;
int T;
int dp[10][10];
bool seen[10][10];
vector<int> samples[55];  
int R[55];
pair<int, int> poss_package(int a, int r)
{
	pair<int, int> A = {2000000, 0};
	for(int i=1; i<=1000000; i++)
	{
		double left = 0.9*(double)i*(double)R[r]- EPS;
		double right = 1.1*(double)i*(double)R[r]+ EPS;
		if(left <= a && a<= right)
		{
			A.first = min(A.first, i);
			A.second = max(A.second, i);
		}
	}
	return A;
}
bool makes_set(int a, int b)
{
	pair<int, int> A = poss_package(a, 0);
	pair<int, int> B = poss_package(b, 1);
	if(A.first<=B.second && B.first <= A.second) return true;
	return false;
}
int solve(int a, int b)
{
	if(a>= samples[0].size() || b>= samples[1].size()) return 0;
	if(seen[a][b]) return dp[a][b];
	seen[a][b] = true;
	if(makes_set(samples[0][a], samples[1][b]))
	{
		dp[a][b] = max(dp[a][b], solve(a+1, b+1)+1);
	}
	dp[a][b] = max(dp[a][b], solve(a+1, b));
	dp[a][b] = max(dp[a][b], solve(a, b+1));
	return dp[a][b];
}
int main()
{
	freopen("infile.txt", "r", stdin);
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		for(int a=0; a<10; a++)
		{
			for(int b=0; b<10; b++)
			{
				seen[a][b] = false;
				dp[a][b] = 0;
			}
		}
		int N, P;
		int ans = 0;
		scanf("%d %d", &N, &P);
		for(int n=0; n<N; n++)
		{
			scanf(" %d ", &R[n]);
		}
		for(int n=0; n<N; n++)
		{
			samples[n].clear();
			for(int p=0; p<P; p++)
			{
				int I;
				scanf("%d", &I);
				samples[n].push_back(I);
			}
			sort(samples[n].begin(), samples[n].end());
		}
		if(N==2) ans = solve(0, 0);
		else 
		{
			for(auto a: samples[0])
			{
				pair<int, int> A = poss_package(a, 0);
				if(A.first <= A.second) 
				{
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
}