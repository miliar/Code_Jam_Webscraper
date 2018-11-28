#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string.h>

#include <vector>
#include <limits>
#include <queue>
#include <cstdlib>
#include <map>
#include <math.h>
#include <limits>
#include <time.h>
#include <bitset>
#include <set>
#include <stack>
#include <iomanip>
#include <complex>
#include <ctime>
using namespace std;
#define ll long long

#define endl '\n'

int n, R, O, Y, G, B, V;
int C[6];
char cad[10005];

char CAR(int v) {
	if (v == 0) return 'R';
	if (v == 1) return 'B';
	if (v == 2) return 'Y';
	if (v == 3) return 'O';
	if (v == 4) return 'G';
	if (v == 5) return 'V';

	return '-';
}

int id[6];
int cmp(int i,int j) {
	return C[i] > C[j];
}

char perm[6];

bool valid() {
	for(int i=0;i<n;i++)
		if (cad[i] == (cad[ (i-1+n) % n ]) || cad[i] == cad[(i+1) % n])
			return false;
	return true;
}

void solve() {
	cin >> n >> R >> O >> Y >> G >> B >> V;

	cad[n] = '\0';
	for(int start=0;start<6;start++) {
		C[0] = R;
		C[1] = B;
		C[2] = Y;
		C[3] = O;
		C[4] = G;
		C[5] = V;


		if (C[start] == 0) continue;

		int izq = 0, der = n - 1;

		cad[izq++] = CAR(start);
		C[start]--;

		int last = start;
		while (C[0] > 1 || C[1] > 1 || C[2] > 1 || C[3] > 1 || C[4] > 1 || C[5] > 1) {
			for(int i=0;i<6;i++) id[i] = i;
			sort(id, id + 6, cmp);

			if (C[ id[1] ] == 0) break;

			if (id[0] != last) {
				last = id[0];
				C[last] -= 2;
				cad[izq++] = cad[der--] = CAR(last);

			} else {
				if (C[ id[1] ] < 2) break;

				last = id[1];
				C[last] -= 2;
				cad[izq++] = cad[der--] = CAR(last);
			}
		}

		if (C[0] > 1 || C[1] > 1 || C[2] > 1 || C[3] > 1 || C[4] > 1 || C[5] > 1) continue;

		int m = 0;

		if (C[0] > 0) perm[m++] = CAR(0);
		if (C[1] > 0) perm[m++] = CAR(1);
		if (C[2] > 0) perm[m++] = CAR(2);
		if (C[3] > 0) perm[m++] = CAR(3);
		if (C[4] > 0) perm[m++] = CAR(4);
		if (C[5] > 0) perm[m++] = CAR(5);

		if (m == 0) {
			cout << cad << endl;
			return;
		}
		else {


			do {
				for(int i=0;i<m;i++) cad[izq + i] = perm[i];

				//cout << "PERM:  " << cad << endl;

				if (valid()) {
					cout << cad << endl;
					return;
				}
			} while (next_permutation(perm, perm + m));
		}
	}

	cout << "IMPOSSIBLE" << endl;
}

int main(){
	//freopen("/Users/jcfernandez/Downloads/CodeJam/input.txt", "r", stdin);
	//freopen("/Users/jcfernandez/Downloads/CodeJam/output.txt", "w", stdout);


	int cas, caso = 1;
	cin >> cas;
	while(cas--) {
		cout << "Case #" << caso++ << ": ";
		solve();
	}
	return 0;
}
