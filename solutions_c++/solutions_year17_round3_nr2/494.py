#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)

struct P
{
	int g, pocz, kon;
	
	bool operator < (const P& dane) const
	{
		return pocz < dane.pocz;
	}
	
	friend istream& operator >> (istream& wejscie, P& dane)
	{
		wejscie >> dane.pocz >> dane.kon;
		return wejscie;
	}
};

const int MAX = 205, DOBA = 24 * 60;
int n, suma_przedz[2], suma_dziur[2], liczba_zmian, liczba_dziur, dziura[MAX];
P p[MAX + 1];

void wczytaj_dane()
{
	int ac, aj;
	cin >> ac >> aj;
	n = 0;
	while (ac--)
	{
		p[n].g = 0;
		cin >> p[n++];
	}
	while (aj--)
	{
		p[n].g = 1;
		cin >> p[n++];
	}
}

void przygotuj_p()
{
	sort(p, p + n);
	p[n] = p[0];
	p[n].pocz += DOBA;
	p[n].kon += DOBA;
}

void wypelnij_suma()
{
	REP(q, 2)
		suma_przedz[q] = suma_dziur[q] = 0;
	liczba_zmian = 0;
	REP(i, n)
	{
		suma_przedz[p[i].g] += p[i].kon - p[i].pocz;
		if (p[i].g == p[i + 1].g)
			suma_dziur[p[i].g] += p[i + 1].pocz - p[i].kon;
		else
			liczba_zmian++;
	}
	assert(liczba_zmian % 2 == 0);
}

void zamien_graczy()
{
	FOR(i, 0, n)
		p[i].g = 1 - p[i].g;
	swap(suma_przedz[0], suma_przedz[1]);
	swap(suma_dziur[0], suma_dziur[1]);
}

void wypelnij_dziura()
{
	liczba_dziur = 0;
	REP(i, n)
		if (p[i].g == 0 && p[i + 1].g == 0)
			dziura[liczba_dziur++] = p[i + 1].pocz - p[i].kon;
}

int wypelnij_dziury()
{
	wypelnij_dziura();
	sort(dziura, dziura + liczba_dziur);
	int w = 0;
	while (suma_przedz[0] + suma_dziur[0] > DOBA / 2)
	{
		assert(liczba_dziur > 0);
		suma_dziur[0] -= dziura[--liczba_dziur];
		w += 2;
	}
	return w;
}

int rozwiaz()
{
	int w = liczba_zmian;
	REP(q, 2)
		if (suma_przedz[q] + suma_dziur[q] > DOBA / 2)
		{
			if (q == 1)
				zamien_graczy();
			w += wypelnij_dziury();
		}
	return w;
}

int zrob_test()
{
	wczytaj_dane();
	przygotuj_p();
	wypelnij_suma();
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
