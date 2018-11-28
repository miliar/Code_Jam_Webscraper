#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <utility>
#include <iomanip> 
#include <queue>

using namespace std;

#define pb push_back

#define N 1010
#define eps 1e-10

typedef long long ll;

int n, k, t;
double u, p[N];

bool check(double pmin)	{
	double ucur = u;
	for (int i = 0; i < n; i++)
	{
		if (p[i] >= pmin)
			continue;
		ucur -= (pmin-p[i]);
	}
	return ucur > 0;
}

int main() {

	//freopen("A-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(false);

	cin >> t;
	int testcase = 0;
	while (t--)	{
		cin >> n >> k;
		cin >> u;
		for (int i = 0; i < n; i++)
			cin >> p[i];
		
		double l = 0.0, r = 1.0;
		
		while (r - l > eps)
		{
			double temp = (l+r)/2.0;
			
			if (check(temp))
				l = temp;
			else
				r = temp;
		}
		
		for (int i = 0; i < n; i++)
			p[i] = max(p[i],l);
			
		double ans = 1.0;
		for (int i = 0; i < n; i++)
			ans *= p[i];
		
		testcase++;
		cout << "Case #" << testcase << ": ";
		cout << setprecision(10) << fixed << ans << endl;
	}

	return 0;
}