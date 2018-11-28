#include <iostream>
#include <cstdio>
using namespace std;

#define ll long long

int T;
ll N, M, maxs, mins;

void Solve(ll N, ll M)
{
	if (M == 1)
	{
		maxs = N / 2;
		mins = (N-1) / 2;
		return;
	}
	ll LS = (N-1) / 2, RS = N / 2;
	M--;
	if (M & 1) Solve(RS, (M+1) / 2);
	else Solve(LS, M/2);
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	scanf("%d", &T);
	for (int id = 1; id <= T; id++)
	{
		printf("Case #%d: ", id);
		cin >> N >> M;
		maxs = mins = 0;
		Solve(N, M);
		cout << maxs << ' ' << mins << endl;
	}
	return 0;
}
