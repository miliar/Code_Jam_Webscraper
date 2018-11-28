#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

long long N, K;

void Recurse(long long N, long long K)
{
	// ceil((N - 1) / 2) + 1 + floor((N - 1) / 2)
	// ceil((K - 1) / 2) + 1 + floor((K - 1) / 2)
	long long RN = (N - 1) / 2;
	long long LN = (N - 1) - RN;
	long long RK = (K - 1) / 2;
	long long LK = (K - 1) - RK;
	if (K == 1)
	{
		cout << LN << " " << RN << endl;
		return;
	}
	if (K % 2 == 0)
		Recurse(LN, LK);
	else
		Recurse(RN, RK);
}

void Work()
{
	cin >> N >> K;
	Recurse(N, K);
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		Work();
		fflush(stdout);
	}
	return 0;
}