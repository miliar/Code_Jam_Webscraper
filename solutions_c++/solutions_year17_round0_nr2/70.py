#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

long long N, Ans;
long long Base[19];

void DFS(int p, long long Cur, int Last)
{
	if (p == -1)
	{
		Ans = Cur;
		return;
	}
	for (int i = 9; i >= Last; i --)
	{
		long long Tmp = Cur;
		for (int l = p; l >= 0; l --)
			Tmp += Base[l] * i;
		if (Tmp <= N)
		{
			DFS(p - 1, Cur + Base[p] * i, i);
			break;
		}
	}
}

void Work()
{
	cin >> N;
	Ans = -1;
	Base[0] = 1;
	for (int i = 1; i < 19; i ++)
		Base[i] = Base[i - 1] * 10;
	DFS(17, 0, 0);
	cout << Ans << endl;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
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