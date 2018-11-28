#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"

using namespace std;

typedef long long ll;
typedef long double ld;

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	int caso = 1;
	while (t--){
		ll n;
		cin >> n;
		ll atual = 0;
		bool aumentou = true;
		while (aumentou){
			aumentou = false;
			
			ll soma = 1;
			ll qtd = 0;
			while (qtd <= 18 &&  atual + soma <= n){
				if ((atual / soma) % 10 == 9) break; 
				//cout << atual << " " << soma << endl;
				aumentou = true;
				atual += soma;
				qtd++;
				soma *= 10LL;
			}
		}
		cout << "Case #" << caso << ": " << atual << endl;
		caso++;
	}
	return 0;
}
