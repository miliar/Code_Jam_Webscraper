#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

int main() {
	int tests;
	cin >> tests;
	fori(caso, 1, tests + 1) {
		string palavra;
		cin >> palavra;
		int k; cin >> k;
		int resposta = 0;
		int n = palavra.size();
		fori(i, 0, n - k + 1) {
			if(palavra[i] == '-') {
				resposta++;
				fori(h, i, i + k) {
					if(palavra[h] == '-') palavra[h] = '+';
					else palavra[h] = '-';
				}
			}
		}
		if(count(palavra.begin(), palavra.end(), '-') > 0) {
			cout << "Case #" << caso << ": IMPOSSIBLE" << '\n';
		}
		else {
			cout << "Case #" << caso << ": " << resposta << '\n';
		}
	}

	return 0;
}

