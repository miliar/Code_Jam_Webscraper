#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main()
{
	int t, casecnt = 1;
	scanf("%d", &t);
	while(t--)
	{
		int n, k;
		double u;
		scanf("%d %d %lf", &n, &k, &u);

		vector<double> p;
		for (int i = 0; i < n; i++)
		{
			double x;
			scanf("%lf", &x);
			p.pb(x);
		}
		sort(p.begin(), p.end());
		p.pb(1.0);
		for (int i = 1; i < p.size() and u > 0.0; i++)
		{
			if (p[i] != p[i-1])
			{
				double rem = p[i] - p[i-1];
				int qtd = i;
				
				double give = min(u, qtd * rem);
				u -= give;
				for (int j = 0; j < i; j++)
					p[j] += give / (1.0 * i);
			}
		}

		double ans = 1.0;
		for (int i = 0; i < n; i++)
		{
			ans *= p[i];
		}
		printf("Case #%d: %lf\n", casecnt++, ans);
	}
	return 0;
}


