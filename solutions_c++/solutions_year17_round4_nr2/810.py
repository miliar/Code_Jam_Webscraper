#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)
#define POKAZ(x) cerr << #x << " = " << (x) << '\n'

const int MAX_N = 1010;
int N, licz[2][MAX_N], suma[2];

void wyczysc_licz()
{
	REP(q, 2)
		REP(i, MAX_N)
			licz[q][i] = 0;
}

void wyczysc_suma()
{
	REP(q, 2)
		suma[q] = 0;
}

void przygotuj_sie()
{
	wyczysc_licz();
	wyczysc_suma();
}

void wczytaj_dane()
{
	int C, M;
	cin >> N >> C >> M;
	assert(C == 2);
	while (M--)
	{
		int P, B;
		cin >> P >> B;
		licz[--B][--P]++;
		suma[B]++;
	}
}

void zamien_klientow()
{
	swap(suma[0], suma[1]);
	REP(i, N)
		swap(licz[0][i], licz[1][i]);
}

int min_liczba_rownych_par(int konflikty)
{
	int w = 0;
	FOR(i, 1, N - 1)
		w = max(w, max(0, licz[1][i] - (suma[0] - konflikty - licz[0][i])));
	return w;
}

void rozwiaz()
{
	int konflikty = max(0, licz[1][0] - (suma[0] - licz[0][0]));
	REP(q, 2)
		licz[q][0] -= konflikty;
	cout << suma[0] + konflikty << ' ' << min_liczba_rownych_par(konflikty) << '\n';
}

void zrob_test()
{
	przygotuj_sie();
	wczytaj_dane();
	if (suma[0] < suma[1])
		zamien_klientow();
	rozwiaz();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	FOR(t, 1, T)
	{
		cout << "Case #" << t << ": ";
		zrob_test();
	}
	return 0;
}
