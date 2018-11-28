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
#define vpi vector<pair<int,int> >
#define vpl vector<pair<long long, long long> >
#define pl pair<long long, long long>
#define fi first
#define sc second
#define pb push_back
#define ul unsigned long long

using namespace std;

ul t, n, k;

int main() {
    
    cin >> t;
    fora(testcase,1,t) {
        cin >> n >> k;
        map<ul,ul> s;
        s[n] = 1;
        while (true) {
            auto p = *--s.end();
            ul m = p.first, r = p.second;
            s.erase(m);
            
            if (r >= k) {
                cout << "Case #" << testcase << ": " << m/2 << " " << (m-1)/2 << endl;
                break;
            }
            
            k -= r;
            s[m/2] += r;
            s[(m-1)/2] += r;
        }
    }

	return 0;
}

