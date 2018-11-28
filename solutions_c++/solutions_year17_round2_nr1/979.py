#include <bits/stdc++.h>
#define fori(_i,_x) for (int _i = 0; _i < _x; ++_i)
#define fora(_i,_a,_b) for (int _i = _a; _i <= _b; ++_i)
#define forb(_i,_b,_a) for (int _i = _b; _i >= _a; --_i)
#define ll long long
#define inf 1000000000
#define vi vector<int>
#define vvi vector<vector<int> >
#define vl vector<long long>
#define pi pair<int,int>
#define vpi vector<pair<double,double> >
#define vpl vector<pair<long long, long long> >
#define pl pair<long long, long long>
#define fi first
#define sc second
#define pb push_back

using namespace std;

int t, d, n;
vpi v;

int main() {
    
    cin >> t;
    fora(test,1,t) {
        cin >> d >> n;
        v.resize(n);
        fori(i,n) cin >> v[i].fi >> v[i].sc;
        sort(v.begin(), v.end());
        
        double u = 0;
        forb(i,n-1,0) {
            u = max(u, (d-v[i].fi)/v[i].sc);
        }
        
        cout << fixed << setprecision(6) << "Case #" << test << ": " << d/u << endl;
    }

	return 0;
}

