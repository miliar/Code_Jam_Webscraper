#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>      // std::setprecision
#include < queue>

#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define endl '\n'
double PI = 3.14159265358979323846264338327950288419716939937510L;
using dvojice = pair<long long int, long long int>;
using ll = long long;

ll a, b, c, d, m, n, x, y;

vector< vector< int >>graf;
vector<int> navstiven;

struct Vrstva {
	ll vyska;
	ll polomer;
	ll Plochasteny() { return polomer*vyska*2; };
	ll Plochahrejsku() { return polomer*polomer; }

};

int main() {
	std::ios::sync_with_stdio(false);


	ll a, b, c, d, m, n, x, y,t,k;
	cin >> t;  
	for (ll i = 1; i <= t; ++i) {
		cin >> n >> k;  // read n and then m.
		vector<Vrstva> vrstvy(n);

		for (ll j = 0; j < n; j++)
		{
			cin >> a >> b;
			vrstvy[j].polomer = a;
			vrstvy[j].vyska = b;
		}
		sort(vrstvy.begin(), vrstvy.end(), [](Vrstva& a, Vrstva& b) {return a.polomer > b.polomer; });

		vector<vector<ll>> tabulka(n + 1, vector<ll>(k + 1));
		vector<vector<ll>> tabulkahrejsku(n + 1, vector<ll>(k + 1, 0));
		for (ll ii = 0; ii < n; ii++)
		{
			tabulka[ii][0] = 0;
		}

		for (ll ii = 0; ii <= k; ii++)
		{
			tabulka[n][ii] = 0;
		}

		for (ll ii = n-1; ii >=0 ; ii--)
		{
			for (ll pocet = 1; pocet <= k; pocet++)
			{
				if (pocet == k) {

					if (tabulka[ii + 1][pocet] >= tabulka[ii + 1][pocet - 1] + vrstvy[ii].Plochasteny() + vrstvy[ii].Plochahrejsku() - tabulkahrejsku[ii + 1][pocet - 1]) {
						tabulka[ii][pocet] = tabulka[ii + 1][pocet];
						tabulkahrejsku[ii][pocet] = tabulkahrejsku[ii + 1][pocet];

					}
					else {
						tabulka[ii][pocet] = tabulka[ii + 1][pocet - 1] + vrstvy[ii].Plochasteny() + vrstvy[ii].Plochahrejsku() - tabulkahrejsku[ii + 1][pocet - 1];
						tabulkahrejsku[ii][pocet] = vrstvy[ii].Plochahrejsku();
					}
					if (tabulka[ii + 1][pocet] == 0) break;
				}
				else {
					if (tabulka[ii + 1][pocet] - tabulkahrejsku[ii + 1][pocet] >= tabulka[ii + 1][pocet - 1] + vrstvy[ii].Plochasteny() - tabulkahrejsku[ii + 1][pocet - 1]) {
						tabulka[ii][pocet] = tabulka[ii + 1][pocet];
						tabulkahrejsku[ii][pocet] = tabulkahrejsku[ii + 1][pocet];

					}
					else {
						tabulka[ii][pocet] = tabulka[ii + 1][pocet - 1] + vrstvy[ii].Plochasteny() + vrstvy[ii].Plochahrejsku() - tabulkahrejsku[ii + 1][pocet - 1];
						tabulkahrejsku[ii][pocet] = vrstvy[ii].Plochahrejsku();
					}
					if (tabulka[ii + 1][pocet] == 0) break;

				}
			}
		}




	cout << "Case #" << i << ": " << setprecision(7) << fixed << tabulka[0][k]*PI << endl;
		
	}
	return 0;
}