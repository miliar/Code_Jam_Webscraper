#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define mp make_pair 

int main() {
	int tests, t;
	cin >> tests;
	for(t = 1; t <= tests; t++) {
		int n, s;
		ll k, d;
		cin >> d >> n;
		vi pos;
		vi speeds;
		for(int i = 0; i < n; i++) {
			cin >> k >> s;
			pos.pb(k);
			speeds.pb(s);
		}
		ld max = 0.0;
		ld aux;
		for(int i = 0; i < n; i++) {
			aux = (ld)(d - pos[i])/speeds[i];
			if(aux > max)
				max = aux;
		}
		aux = (ld)d/max;
		cout << fixed;
    	cout << setprecision(6);
		cout << "Case #" << t << ": " << aux << endl;
	}
	return 0;
}