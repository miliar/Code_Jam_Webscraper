#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef long double LD;
#define FOR(x, a, b) for (LL x = (a); x <= (b); x++)
#define REP(x, n) for (LL x = 0; x < (n); x++)

const LL MAX_N = 1010;
const LD INF = 1e15;
LL D, N, K[MAX_N], S[MAX_N];

void wczytaj_dane()
{
	cin >> D >> N;
	REP(i, N)
		cin >> K[i] >> S[i];
}

LD nie_przegon_konia(LL i)
{
	return LD(D * S[i]) / LD(D - K[i]);
}

LD rozwiaz()
{
	LD w = INF;
	REP(i, N)
		w = min(w, nie_przegon_konia(i));
	return w;
}

LD zrob_test()
{
	wczytaj_dane();
	return rozwiaz();
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	LL T;
	cin >> T;
	cout.setf(ios::fixed);
	cout.precision(20);
	FOR(t, 1, T)
		cout << "Case #" << t << ": " << zrob_test() << '\n';
	return 0;
}
