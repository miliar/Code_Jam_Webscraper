#include <iostream>
#include <stdio.h>
#include <queue>
#include <string.h>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);cin.tie(NULL);

	int TC, t;
	int d, n, k, s;
	double tt, aux;

	cin >> TC;
	t = 1;

	
	while( t <= TC ){
		cin >> d >> n;

		tt = 0.0;

		while( n-- ){
			cin >> k >> s;
			aux = (double) ( d - k )/ (double)s;
			tt = max(aux, tt);
		}

		aux = (double) d / tt;

		printf("Case #%d: %.6f\n", t, aux);
		t++;
	}
	
	return 0;
}