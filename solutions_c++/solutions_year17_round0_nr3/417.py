#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"

using namespace std;

typedef long long ll;
typedef long double ld;

vector<pair<ll, ll> > v, aux;
bool cmp(pair<ll, ll> a, pair<ll, ll> b){
	if (a.fi == b.fi) return a.se < b.se;
	return a.fi > b.fi;
}
int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	int caso = 0;
	while (t--){
		v.clear();
		caso++;
		ll n, k;
		cin >> n >> k;
		
		ll atual = 0;
		v.pb(mp(n, 1));
		while (1){
			//cout << "Aqui " << endl;
			//int bb;
			//cin >> bb;
			//for (int i = 0; i < v.size(); i++){
			//	cout << v[i].fi << " " << v[i].se << endl;
			//}
			//cout << "QTD " << atual << endl;
			aux.clear();
			bool br = false;
			for (int i = 0; i < v.size(); i++){
				ll l, r;
				ll qtd = v[i].se;
				ll val = v[i].fi;
				if (val == 0) continue;
				l = (val + 1) / 2;
				r = val / 2;
				l--;
				if (atual + qtd >= k){
					cout << "Case #" << caso << ": " << r << " " << l << endl;
					br = true;
					break;
				} 
				atual += qtd;
				//cout << "Pusha " << l << " " << r <<  " " << qtd << endl;		
				aux.pb(mp(l, qtd));
				aux.pb(mp(r, qtd));
			}
			if (br) break;
			
			sort(aux.begin(), aux.end(), cmp);
			v.clear();
			ll atual = aux[0].fi;
			ll qtd = 0;
			for (int i = 0; i < aux.size(); i++){
				if (atual == aux[i].fi){
					qtd += aux[i].se;
				} 
				else{
					v.pb(mp(atual, qtd));
					atual = aux[i].fi;
					qtd = aux[i].se;
				}
			}
			v.pb(mp(atual, qtd));
		}
	}
	return 0;
}

