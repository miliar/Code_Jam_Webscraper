#include <bits/stdc++.h>
using namespace std;

int main (){

	freopen("A-large.in", "r", stdin);
	freopen("solLarge.out", "w", stdout);
	int t;
	cin >> t;
	for (int caso = 1; caso <= t; caso++){
		string cad;
		int k;
		cin >> cad;
		cin >> k;
		vector <int> suma(cad.size() + 10);
		int cont = 0;
		bool posible = true;
		int res = 0;
		for (int i = 0; i < cad.size(); i++){
			cont += suma[i];
			char act;
			if (cad[i] == '+'){
				if (cont % 2) act = '-';
				else act = '+';
			}else{
				if (cont % 2) act = '+';
				else act = '-';
			}
			if (act == '-'){
				if (i + k - 1 < cad.size()){
					cont++;
					res++;
					suma[i + k]--;
				}else{
					posible = false;
				}
			}
		}
		cout << "Case #" << caso << ": ";
		if (posible) cout << res << "\n";
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}