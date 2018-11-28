#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
long long int d, n;
long long int k[1200];
long long int s[1200];

bool isgood(double now)
{
	for (int i = 0; i < n; i++)
	{
		if ((double)s[i] > now) continue;
		if (now * k[i] > d * (now - s[i])) continue;
		return false;
	}
	return true;
}

void solve(int casen)
{
	cin >> d >> n;
	for (int i = 0; i < n; i++) cin >> k[i] >> s[i];
	double now = (double)d*s[0] / (d - k[0]);
	for (int i = 0; i < n; i++)
	{
		now = min(now, (double)d*s[i] / (d - k[i]));	
	}
	printf("Case #%d: %lf\n", casen, now);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
}