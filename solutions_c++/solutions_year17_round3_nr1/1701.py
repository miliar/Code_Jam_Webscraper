#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pll pair <ll , ll>
#define NMAX 1000

int N, K;
vector < pair < double , double > > v;

double dp[NMAX + 1][NMAX + 1];

double area(double r, double h)
{
	double a = M_PI * r * r + 2.0 * M_PI * r * h;
	return a;
}
double disk(double r, double h)
{
	//if(h == 1.0) return 0.0;
	return M_PI * r * r;
}

double solve(int i, int k)
{
	//cout << i << " " << k << endl;
	if( k <= 0 || i <= 0 ) return 0.0;
	//if(k == 1) return dp[i][k] = area(v[i].first, v[i].second);
	if(dp[i][k] != 0.0) return dp[i][k];

	double ar = area(v[i].first, v[i].second);
	double ans = ar;

	for(int j = i - 1; j >= 1; j-- )
		ans = max(ans, max( ar + solve(j, k - 1) - disk(v[j].first, v[j].second),  solve( j, k ) ) );
	
	return dp[i][k] = ans;
}
int main()
{
	//freopen("A-small-attempt2.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d\n",&T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);

		cin >> N >> K;
		v.push_back(make_pair(0.0,0.0));
		for(int i = 1; i <= N; i++)
		{
			double r, h;
			scanf("%lf %lf",&r,&h);
			v.push_back(make_pair(r, h));
		}

		for(int i = 0; i <= NMAX; i++) for(int j = 0; j <= NMAX; j++) dp[i][j] = 0.0;

		sort(v.begin(), v.end());

		solve(N, K);
	
		printf("%0.8lf\n",dp[N][K]);
		//cout << "Testcase " << t << " solved!\n\n";
		v.clear();
	}
	return 0;
}
