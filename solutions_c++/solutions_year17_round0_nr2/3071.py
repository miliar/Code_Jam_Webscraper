#include <bits/stdc++.h>
using namespace std;

int vis[22][12][4];
int decision[22][12][4];
int posN[22][12][4];
int mayorN[22][12][4];
int bajeN[22][12][4];
int memo[22][12][4];
int color;
string cad;

int dp (int pos, int mayor, int baje){
	if (pos == cad.size())
		return 1;
	if (vis[pos][mayor][baje] != color){
		vis[pos][mayor][baje] = color;
		int res = 0;
		if (baje){
			for (int i = mayor; i <= 9; i++){
				int act = dp(pos + 1, i, baje);
				if (act){
					decision[pos][mayor][baje] = i;
					posN[pos][mayor][baje] = pos + 1;
					mayorN[pos][mayor][baje] = i;
					bajeN[pos][mayor][baje] = baje;
					res = max(res, act);
				}
			}
		}else{
			for (int i = mayor; i <= cad[pos] - '0'; i++){
				int act = dp(pos + 1, i, (i < cad[pos] - '0') ? 1 : 0);
				if (act){
					decision[pos][mayor][baje] = i;
					posN[pos][mayor][baje] = pos + 1;
					mayorN[pos][mayor][baje] = i;
					bajeN[pos][mayor][baje] = (i < cad[pos] - '0') ? 1 : 0;
					res = max(res, act);
				}
			}
		}
		memo[pos][mayor][baje] = res;
	}
	return memo[pos][mayor][baje];
}

int main (){

	freopen("B-large.in", "r", stdin);
	freopen("solLarge.out", "w", stdout);
	int casos;
	cin >> casos;
	for (int t = 1; t <= casos; t++){
		cin >> cad;
		color++;
		cout << "Case #" << t << ": ";
		int posible = dp (0, 1, 0);
		if (posible){
			int pos = 0;
			int mayor = 1;
			int baje = 0;
			int cont = 0;
			while (cont < cad.size()){
				cout << decision[pos][mayor][baje];
				int auxPos = posN[pos][mayor][baje];
				int auxMayor = mayorN[pos][mayor][baje];
				int auxBaje = bajeN[pos][mayor][baje];
				pos = auxPos;
				mayor = auxMayor;
				baje = auxBaje;
				cont++;
			}
			cout << "\n";
		}else{
			for (int i = 0; i < cad.size() - 1; i++)
				cout << "9";
			cout << "\n";
		}
	}
	return 0;
}