#include <bits/stdc++.h>
using namespace std;

typedef long double LD;
#define FOR(x, a, b) for (int x = (a); x <= (b); x++)
#define REP(x, n) for (int x = 0; x < (n); x++)

struct Ciasto
{
	LD R, H;
	
	bool operator < (const Ciasto& dane) const
	{
		return R > dane.R;
	}
	
	LD bok() const
	{
		return 2 * M_PI * R * H;
	}
	
	LD pole_podstawy() const
	{
		return M_PI * R * R;
	}
	
	friend istream& operator >> (istream& wejscie, Ciasto& dane)
	{
		wejscie >> dane.R >> dane.H;
		return wejscie;
	}
};

const int MAX = 1010;
int N, K, kol[MAX];
Ciasto pan[MAX];

void wczytaj_dane()
{
	cin >> N >> K;
	REP(i, N)
		cin >> pan[i];
}

int porz_bok(int a, int b)
{
	return pan[a].bok() > pan[b].bok();
}

void wypelnij_kol()
{
	REP(i, N)
		kol[i] = i;
	sort(kol, kol + N, porz_bok);
}

LD zacznij_od(int i)
{
	LD w = pan[i].pole_podstawy() + pan[i].bok(), poz = K - 1;
	REP(j, N)
	{
		int k = kol[j];
		if (poz > 0 && i < k)
		{
			w += pan[k].bok();
			poz--;
		}
	}
	assert(poz == 0);
	return w;
}

LD rozwiaz()
{
	LD w = 0.0;
	FOR(i, 0, N - K)
		w = max(w, zacznij_od(i));
	return w;
}

LD zrob_test()
{
	wczytaj_dane();
	sort(pan, pan + N);
	wypelnij_kol();
	return rozwiaz();
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
