#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

long long consone[20]; // consequent 1s

void init()
{
	consone[1] = 1;
	for (int i = 2; i <= 18; i++) consone[i] = consone[i - 1] * 10 + 1;
}

long long getAnswer(long long in)
{
	long long cum = 0; int pos = 18, addcnt = 0;
	while (pos > 0 && addcnt <= 8)
	{
		while (cum + consone[pos] <= in && addcnt <= 8)
		{
			cum += consone[pos];
			addcnt++;
		}
		pos--;
	}
	return cum;
}

void solve(int casen)
{
	long long in; scanf("%lld", &in);
	long long ans = getAnswer(in);
	printf("Case #%d: %lld\n", casen, ans);
}

int main()
{
	init();
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
}