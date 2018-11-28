#include <bits/stdc++.h>
using namespace std;

typedef long double LD;
#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)

const int MAX = 53;
const LD EPS = 1e-9;
int N, K;
LD U, P[MAX];

void wczytaj_dane()
{
	cin >> N >> K >> U;
	assert(N == K);
	REP(i, N)
		cin >> P[i];
}

int przelewa_sie()
{
	LD suma = 0.0;
	REP(i, N)
	{
		if (U + EPS < i * P[i] - suma)
			return i;
		suma += P[i];
	}
	return N;
}

void wyrownaj(int p)
{
	REP(i, p)
	{
		U -= P[p - 1] - P[i];
		P[i] = P[p - 1];
	}
}

void dolej(int p)
{
	REP(i, p)
	{
		P[i] += U / p;
		assert(P[i] < 1.0 + EPS);
	}
	U = 0.0;
}

void rozwiaz()
{
	int p = przelewa_sie();
	assert(p > 0);
	wyrownaj(p);
	dolej(p);
}

LD oblicz_wynik()
{
	LD w = 1.0;
	REP(i, N)
		w *= P[i];
	return w;
}

LD zrob_test()
{
	wczytaj_dane();
	sort(P, P + N);
	rozwiaz();
	return oblicz_wynik();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	cout.setf(ios::fixed);
	cout.precision(9);
	FOR(t, 1, T)
		cout << "Case #" << t << ": " << zrob_test() << '\n';
	return 0;
}
