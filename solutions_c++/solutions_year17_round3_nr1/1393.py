#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
typedef long long ll;
typedef std::pair<ll, ll> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(long long i = 0; i < (long long)N; i++)
#define fornj(N)         for(long long j = 0; j < (long long)N; j++)
#define fornk(N)         for(long long k = 0; k < (long long)N; k++)
#define foreach(c,itr)   for(auto itr=(c).begin();itr!=(c).end();itr++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define v vector
using namespace std;

bool cmp(pii a, pii b)
{
	double contriba = a.second * (2 * PI*a.first);
	double contribb = b.second * (2 * PI*b.first);
	return contriba < contribb;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (size_t t = 1; t <= T; t++)
	{
		int N, K;
		cin >> N >> K;
		v<pii> r(N);
		for (size_t i = 0; i < N; i++)
		{
			cin >> r[i].first >> r[i].second;
		}
		sort(ALL(r));
		double ans = 0;
		for (int k = K - 1; k < N; k++)
		{
			ll radius = r[k].first;
			sort(r.begin(), r.begin() + k, cmp);
			double sum = 0;
			for (int ii = 0; ii < K; ii++)
			{
				sum += r[k - ii].second * (2 * PI * r[k - ii].first);
			}
			ans = max(ans, radius*radius*PI + sum);
		}
		cout << "Case #" << setprecision(9) << fixed<< t << ": " << ans << endl;
	}

	
	
	return 0;
}