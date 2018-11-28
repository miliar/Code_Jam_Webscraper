#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;

typedef long double ld;
typedef long long ll;

int n;
int d;


void testcase(int tcn){
	cin >> d >> n;

	ld max_t = 0;

	int k, s;

	REP(i, n){
		cin >> k >> s;
		ld t = (d-k)/((ld)s);
		max_t = max(t, max_t);
	}






	cout << "Case #"<< setprecision(12)<<tcn<<": "<<d/max_t<<endl;

}

int main(){
	int T;
	cin >> T;
	REP(i, T){
		testcase(i+1);
	}
	return 0;

}