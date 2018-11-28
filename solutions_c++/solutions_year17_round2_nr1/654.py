#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define oioi printf("oioi\n")
#define eoq cout << "eoq" << '\n'
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;
typedef pair<double, double> dd;
typedef vector<ll> vi;
typedef vector<ii> vii;
const int dx[] = {0 ,1,-1,0,1,-1,-1, 1};
const int dy[] = {-1,0,0, 1,1, 1,-1,-1};
const ll MOD = 0;
const ll N = 0;

int main () {

	ll t;
	cin >> t;
	
	ll d, n, ini, vel;
	for(int tc = 1; tc<=t; tc++){
		cin >> d >> n;
		double tMin = -1.0;
		for (int i = 0; i < n; i++)
		{
			cin >> ini >> vel;
			tMin = max(tMin, (d-ini)*1.0/vel*1.0);
		}
		cout << "Case #" << tc << ": " << fixed << setprecision(10) << (d*1.0/tMin) << endl;
	}
	
	return 0;
}
