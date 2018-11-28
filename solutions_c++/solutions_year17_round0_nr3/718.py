#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
	int T;
	cin >> T;
	for(int l = 1; l <= T; l++){
		ll N, K;
		cin >> N >> K;
		map<ll, ll> mapa;
		mapa[N] = 1LL;
		set<ll> fila;
		set<ll> fila1;
		fila.insert(N);
		mapa[N] = 1LL;
		while(fila.size()){
			fila1.clear();
			for(auto it = fila.begin(); it != fila.end(); it++)
			{
				mapa[(*it - 1)/2LL] += mapa[(*it)];
				mapa[(*it - 1) - (*it - 1)/2LL] += mapa[(*it)];
				if((*it - 1)/2LL > 0LL)
					fila1.insert((*it - 1)/2LL);
				if((*it - 1) - (*it - 1)/2LL > 0LL)
					fila1.insert((*it - 1) - (*it - 1)/2LL);
			}
			fila = fila1;
		}

		auto it = mapa.end();
		ll cont = 0LL;
		while(cont < K){
			it--;
			cont += it->second;
		}
		ll a = (it->first - 1)/2LL, b = (it->first - 1) - (it->first - 1)/2LL;

		cout << "Case #" << l << ": " << b << " " << a << endl;

	}
}