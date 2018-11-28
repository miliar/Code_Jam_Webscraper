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


long double EPS = 1e-6;

int n;
long double D, Ki[1005], Si[1005];

bool test(long double kh) {
	long double T = D / kh;

	for(int i=0;i<n;i++) {
		if (Ki[i] >= D) continue;
		//double pos = Ki[i] + Si[i] * T;
		if (Si[i] < (D - Ki[i]) / T)
			return false;
	}
	return true;
}

void solve() {
	cin >> D >> n;
	//cout << setprecision(3) << D << " " << n << endl;
	for(int i=0;i<n;i++) {
		cin >> Ki[i] >> Si[i];
		//cout << setprecision(3) << Ki[i] << " " << Si[i] << endl;
	}

	long double izq = 0, der = 1e16, med;

	while ( fabs(der - izq) > EPS) {
		med = (izq + der) / 2.0;
		//cout << setprecision(8) << izq << " " << der << " " << med << " " << fabs(der - izq) << endl;
		if (test(med))
			izq = med;
		else
			der = med;
	}
	cout << setprecision(7) << fixed << izq << endl;
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
