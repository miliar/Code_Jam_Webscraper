#include <bits/stdc++.h>
#include <math.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl
#define pb push_back
#define mp make_pair

typedef long long tint;
typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;
typedef unsigned long long utint;
typedef long double ldouble;

typedef vector<int> vint;

int toNumber (string s)
{
	int Number;
	if ( ! (istringstream(s) >> Number) ) Number = 0; // el string vacio lo manda al cero
	return Number;
}

string toString (int number)
{
    ostringstream ostr;
    ostr << number;
    return  ostr.str();
}

tint ele(tint a, tint b){
	if (b == 0) {
		return 1;
	}
	if (b % 2 == 0) {
		return ele(a*a, b/2);
	} else {
		return a * ele(a*a, b/2);
	}
}

tint gcd(tint a, tint b){
	if (a==0) {
		return b;
	}
	return gcd(b % a, a);
}

double d_abs(long a, long b){
	if(a > b){
		return a - b;
	}
	return b - a;
}

int main() {
	tint t;
	cin >> t;
	forn(casen, t) {
		tint D, N;
		cin >> D >> N;	

		vector<double> k(N);
		vector<double> s(N);

		double res = 999999999999999999.0; // REVISAR
		forn(i, N) {
			cin >> k[i] >> s[i];
			double vAn = (D*s[i]) / (D-k[i]);
			res = min(res, vAn);
		}
		std::setprecision(6);
		cout << "Case #" << casen + 1<< ": "<<  std::fixed << std::setprecision(6) << res << endl;

	}
}