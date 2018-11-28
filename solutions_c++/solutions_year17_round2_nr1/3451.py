#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;
typedef pair<double,double> Par;
const double ERROR = 1e-6;

bool Igual(double a,double b){
	return fabs(a-b) < ERROR;
}

bool alcanza(Par a, Par b, double D){
	double x, d;
	x = b.first - a.first;
	d = (a.second*x)/(a.second - b.second) + a.first;

	return d < D || Igual(d,D) ;

}

int main(){

	int T;
	int N;
	double D;
	double vel;
	Par arriba;
	stack<Par> pila;
	vector<Par> caballo;

	optimizar_io(0);

	cin >> T;

	for(int caso = 1 ; caso <= T ; caso++){
		cin >> D >> N ; 

		caballo = vector<Par>(N);

		for(int i = 0 ; i< N ; i ++)
			cin >> caballo[i].first >> caballo[i].second ;
		sort(caballo.begin(),caballo.end());

		pila.push(caballo.back());
		for(int i = N -2 ; i >= 0 ;  i--){
			arriba = pila.top();
			if(caballo[i].second > arriba.second && alcanza(caballo[i],arriba,D)){
				continue;
			} else {
				pila.push(caballo[i]);
			}
		}

		arriba = pila.top();

		vel = (arriba.second * D)/(D-arriba.first);

		cout << "Case #"<< caso << ": "<< setprecision(6) << fixed << vel << '\n' ;

	}

	return 0;
}