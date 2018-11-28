#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <vector>
#include <stack>
#include <algorithm>
#include <cmath>
using namespace std;

#define FOR(i,n,j) for(int i=0 ; i<n ; i+=j)
#define scan(a) scanf("%d", &a)
#define memset(a,b) memeset(a,b,sizeof(a))
#define pb push_back

int main (){
	int cuentas, marcador;
	cin >> cuentas;
	marcador = cuentas;
	while (cuentas--){
		
		double t, maximo = 0, total, d,n, k ,s;
		
		cin >> d >> n;
		//printf ("%Lf %Lf\n", d, n);
		FOR(i,n,1){
			cin >> k >> s;
			//printf ("%Lf %Lf\n", k,s);
			t = (d - k) / s;
			//printf ("%Lf\n", t);
			if ( t > maximo ){
				maximo = t;
			}
		}
		
		total = (d / maximo);
		//printf ( "total: %lf\n", total);
		printf ("Case #%d: %lf\n", marcador-cuentas , total);
	}
}
