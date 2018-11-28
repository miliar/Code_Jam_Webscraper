//Autor: Mateusz Wasylkiewicz
//Zawody: Google Code Jam 2017
//Strona: https://code.google.com/codejam/
//Zadanie: Tidy Numbers (Large), Qualification Round 2017
//Czas: O(T*log^2(N))
#include <bits/stdc++.h>
using namespace std;

#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define FORD(x, a, b) for (int x = (a); x >= (b); x--)
#define REP(x, n) for (int x = 0; x < (n); x++)
#define SIZE(x) int((x).size())

string S;

void wczytaj_dane()
{
	cin >> S;
}

bool czysty_poczatek(int m)
{
	assert(m <= SIZE(S));
	REP(i, m - 1)
		if (S[i] > S[i + 1])
			return false;
	return true;
}

string oblicz_wynik(int m)
{
	FOR(i, m + 1, SIZE(S) - 1)
		S[i] = '9';
	return S.substr(S.find_first_not_of("0"));
}

string rozwiaz()
{
	if (czysty_poczatek(SIZE(S)))
		return S;
	FORD(i, SIZE(S) - 1, 0)
		if (S[i] != '0')
		{
			S[i]--;
			if (czysty_poczatek(i + 1))
				return oblicz_wynik(i);
			S[i]++;
		}
	assert(false);
}

string zrob_test()
{
	wczytaj_dane();
	return rozwiaz();
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(t, 1, T)
		cout << "Case #" << t << ": " << zrob_test() << '\n';
	return 0;
}
