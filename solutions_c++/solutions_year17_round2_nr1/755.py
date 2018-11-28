#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vll;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;
#define pb push_back
#define fst first
#define snd second

int D, N;

void solve()
{
	
	scanf("%d%d", &D, &N);
	double mtime = 0;
	for(int i = 0; i < N; ++i)
	{
		int k, s;
		scanf("%d%d", &k, &s);
		double K = D - k;
		double time = K / s;
		mtime = max(time, mtime);
	}
	double wynik = D / mtime;
	printf("%.13lf\n", wynik);
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solve();
		fprintf(stderr, "Rozwiazano %d\n", i);
	}
	
	
	return 0;
}
