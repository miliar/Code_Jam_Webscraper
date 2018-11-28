//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2017
//Strona: https://code.google.com/codejam/
//Zadanie: Bathroom Stalls (Large), Qualification Round 2017
//Czas: Theta(T*log(N))
#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<LL, LL> PII;
#define FOR(x, a, b) for (LL x = (a); x <= (b); x++)
#define REP(x, n) for (LL x = 0; x < (n); x++)
#define SIZE(x) LL((x).size())
#define PB push_back
#define ST first
#define ND second

LL N, K;
vector<PII> dziury;

void wczytaj_dane()
{
	cin >> N >> K;
}

void dodaj_dziury(LL dl, LL licz)
{
	if (dl == 0)
		return;
	assert(dl <= dziury.back().ST);
	if (dl == dziury.back().ST)
		dziury.back().ND += licz;
	else
		dziury.PB(PII(dl, licz));
}

void wypelnij_dziury()
{
	dziury.clear();
	dziury.PB(PII(N, 1));
	for (LL i = 0; dziury[i].ST > 1; i++)
	{
		LL dl = dziury[i].ST, licz = dziury[i].ND;
		dodaj_dziury(dl / 2, licz);
		dodaj_dziury((dl - 1) / 2, licz);
	}
	
	LL suma = 0;
	REP(i, SIZE(dziury))
	{
		if (i != 0)
			assert(dziury[i - 1].ST > dziury[i].ST);
		assert(dziury[i].ND > 0);
		suma += dziury[i].ND;
	}
	assert(suma == N);
}

void rozwiaz(LL& y, LL& z)
{
	LL i = 0;
	while (dziury[i].ND < K)
	{
		K -= dziury[i++].ND;
		assert(i < SIZE(dziury));
	}
	LL dl = dziury[i].ST;
	y = dl / 2;
	z = (dl - 1) / 2;
}

void zrob_test(LL& y, LL& z)
{
	wczytaj_dane();
	wypelnij_dziury();
	rozwiaz(y, z);
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	LL T;
	cin >> T;
	FOR(t, 1, T)
	{
		LL y, z;
		zrob_test(y, z);
		cout << "Case #" << t << ": " << y << ' ' << z << '\n';
	}
	return 0;
}
