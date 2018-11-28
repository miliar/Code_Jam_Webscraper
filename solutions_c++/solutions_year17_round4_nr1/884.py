#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)
#define POKAZ(x) cerr << #x << " = " << (x) << '\n'

const int MAX_P = 4;
int P, licz[MAX_P];

void wyczysc_licz()
{
	REP(i, MAX_P)
		licz[i] = 0;
}

void wczytaj_dane()
{
	int N;
	cin >> N >> P;
	while (N--)
	{
		int G;
		cin >> G;
		licz[G % P]++;
	}
}

int sufit_ilorazu(int a, int b)
{
	return a % b == 0 ? a / b : a / b + 1;
}

int rozwiaz()
{
	if (P == 2)
		return licz[0] + sufit_ilorazu(licz[1], 2);
	else if (P == 3)
	{
		int mini = min(licz[1], licz[2]), maks = max(licz[1], licz[2]);
		return licz[0] + mini + sufit_ilorazu(maks - mini, 3);
	}
	else
	{
		int w = licz[0], mini = min(licz[1], licz[3]);
		w += (licz[2] / 2);
		licz[2] %= 2;
		w += mini;
		licz[1] -= mini;
		licz[3] -= mini;
		w += sufit_ilorazu(licz[1] + licz[3] + 2 * licz[2], 4);
		return w;
	}
}

int zrob_test()
{
	wyczysc_licz();
	wczytaj_dane();
	return rozwiaz();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	FOR(t, 1, T)
		cout << "Case #" << t << ": " << zrob_test() << '\n';
	return 0;
}
