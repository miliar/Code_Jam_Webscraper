#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 105;

int P, N, G[MAXN], mod[4];
void Solve2()
{
	cout << N - mod[1] / 2 << endl;
}
void Solve3()
{
	int ans = 0;
	int p = mod[1], q = mod[2];
	if (p < q)
		swap(p, q);
	ans += q;
	p -= q;
	ans += p - ((p + 2) / 3);
	cout << N - ans << endl;
}
void Solve4()
{
	int ans = 0;
	int p = mod[1], q = mod[3], r = mod[2];

	if (p < q)
		swap(p, q);
	ans += q;
	p -= q;
	ans += r / 2;
	r %= 2;

	if (p && r)
	{
		if (p >= 2)
		{
			ans += 2; p -= 2;
			ans += p - ((p + 3) / 4);
		}
		else
			++ans;
	}
	else if (p && !r)
		ans += p - ((p + 3) / 4);
	cout << N - ans << endl;
}
void Solve()
{
	cin >> N >> P;
	for (int i = 1; i <= N; ++i)
		cin >> G[i];
	memset(mod, 0, sizeof(mod));
	for (int i = 1; i <= N; ++i)
		++mod[G[i] % P];
	switch (P)
	{
		case 2: Solve2(); break;
		case 3: Solve3(); break;
		case 4: Solve4(); break;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		Solve();
	}
	return 0;
}
