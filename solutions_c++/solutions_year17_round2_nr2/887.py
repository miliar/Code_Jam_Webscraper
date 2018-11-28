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

using namespace std;

int t, n, c[6], bob, rgr, yvy;
char m[6] = {'R','O','Y','G','B','V'};
string out, s[3];

int main() {
    
    cin >> t;
    fora(test,1,t) {
        cin >> n;
        fori(i,6) cin >> c[i];
        
        out = "";
        s[0] = "";
        s[1] = "";
        s[2] = "";
        
        bool done = false;
        
        fori(j,3) {
            int r = j * 2 + 1;
            int k = (r+3)%6;
            if (c[r] + c[k] == n) {
                if (c[r] == c[k]) {
                    cout << "Case #" << test << ": " ;
                    fori(i,c[r]) cout << m[r] << m[k];
                    cout << endl;
                } else {
                    cout << "Case #" << test << ": IMPOSSIBLE" << endl;
                }
                done = true;
                break;
            } else {
                if (c[r] > 0 && c[r] + 1 > c[k]) {
                    cout << "Case #" << test << ": IMPOSSIBLE" << endl;
                    done = true;
                    break;
                }
            }
            fori(i,c[r]) {
                s[j] += m[k];
                s[j] += m[r];
            }
            if (c[r] > 0) s[j] += m[k];
            
            if (c[r] > 0) c[k] -= c[r] + 1;
            c[r] = 0;
        }
        
        if (done) continue;
        
        if (s[0].size() > 0) c[4] += 1;
        if (s[1].size() > 0) c[0] += 1;
        if (s[2].size() > 0) c[2] += 1;
        
        vpi a;
        a.pb(pi(c[4],4));
        a.pb(pi(c[0],0));
        a.pb(pi(c[2],2));
        sort(a.begin(), a.end());
        
//        cout << a[0].fi << " " << a[1].fi << " " << a[2].fi << endl;
        
        if (a[0].fi + a[1].fi < a[2].fi) {
            cout << "Case #" << test << ": IMPOSSIBLE" << endl;
            continue;
        }
        
        fori(i,a[0].fi+a[1].fi - a[2].fi) {
            out += m[a[2].sc];
            out += m[a[1].sc];
            out += m[a[0].sc];
        }
        fori(i,a[2].fi-a[0].fi) {
            out += m[a[2].sc];
            out += m[a[1].sc];
        }
        fori(i,a[2].fi-a[1].fi) {
            out += m[a[2].sc];
            out += m[a[0].sc];
        }
        
//        cout << out << endl << s[0] << endl << s[1] << endl << s[2] << endl;
        
        if (s[0].size() > 0) {
            int q = out.find(m[4]);
            out = out.substr(0,q) + s[0] + out.substr(q+1,out.size()-q-1);
        }
        if (s[1].size() > 0) {
            int q = out.find(m[0]);
            out = out.substr(0,q) + s[1] + out.substr(q+1,out.size()-q-1);
        }
        if (s[2].size() > 0) {
            int q = out.find(m[2]);
            out = out.substr(0,q) + s[2] + out.substr(q+1,out.size()-q-1);
        }
        
        cout << "Case #" << test << ": " << out << endl;
        
//        fori(i,a[0].fi+a[1].fi - a[2].fi) {
//            cout << m[a[2].sc] << m[a[1].sc] << m[a[0].sc];
//        }
//        fori(i,a[2].fi-a[0].fi) {
//            cout << m[a[2].sc] << m[a[1].sc];
//        }
//        fori(i,a[2].fi-a[1].fi) {
//            cout << m[a[2].sc] << m[a[0].sc];
//        }
//        cout << endl;
    }

	return 0;
}

