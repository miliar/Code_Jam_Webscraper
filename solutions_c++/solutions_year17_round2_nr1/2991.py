#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define pii pair<ll, ll>
#define MAXN 1005

using ll = long long;

ll T, N, D;
pii p[MAXN];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> T;
	int casenum = 1;
	while (T--)
	{
		cin >> D >> N;
		for (int i = 0; i < N; ++i)
			cin >> p[i].first >> p[i].second;
		sort(p, p + N);
		double time;
		time = 1.0*(D - p[N - 1].first) / p[N - 1].second;
		for (int i = N - 2; i >= 0; --i)
		{
			//double x = (p[i + 1].first*p[i].second - p[i].first*p[i + 1].second) / (p[i].second - p[i + 1].second);
			//if (x > D)
			if (1.0*(D - p[i].first) / p[i].second > time)
				time = 1.0*(D - p[i].first) / p[i].second;
		}
		printf("Case #%d: %.7f\n", casenum, 1.0*D / time);
		//cout << "Case #" << casenum << ":" << " " << (D / time) << endl;
 		casenum++;
	}
	return 0;
}