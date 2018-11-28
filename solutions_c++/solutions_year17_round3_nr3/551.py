#include <iostream>
#include <cstdio>
#include <iomanip>
#include <queue>
#include <vector>
#include <set>
#define heap priority_queue
#define ld long double
using namespace std;
const int maxn = 50;
const ld eps = 1e-18;
int n,k;
ld u,p[maxn+1];
void solve()
{
	cin >> n >> k >> u;
	ld maxp=0;
	for (int i=1; i<=n; i++)
	{
		cin >> p[i];
		maxp=max(maxp,p[i]);
	}
	ld dau=0,cuoi=1;
	do
	{
		ld giua=(dau+cuoi)/2;
		ld sum=0;
		for (int i=1; i<=n; i++)
			if (p[i]<giua) sum+=(giua-p[i]);
		if (sum<=u) dau=giua+eps;
		else cuoi=giua-eps;
	}
	while (dau-cuoi<=eps);
	for (int i=1; i<=n; i++)
		if (p[i]<cuoi) p[i]=cuoi;
	ld res=1;
	for (int i=1; i<=n; i++)
		res*=p[i];
	cout << setprecision(10) << fixed << res;
}
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i=1; i<=t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}