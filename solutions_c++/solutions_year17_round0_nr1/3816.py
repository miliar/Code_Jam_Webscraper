#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>
#include <queue>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <cassert>
#define MOD (ll)1e9 + 7
#define eps (ld)1e-30
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define sz(a) a.size()
#define loop(i, n) for(long long (i) = 0; (i) < (n) ; ++ (i))
#define loopn()
#define pii pair<int,int>
#define pll pair<long long,long long>
#define pld pair<long double,long double>
#define vii vector<int>
#define vll vector<long long>  
typedef long long ll;
typedef long double ld;
 
using namespace std;
 
/*@Sergey_Miller*/

void revert(string& s, ll p, ll k) {
    loop(i,k) {
        s[p+i] = (s[p+i] == '+' ? '-' : '+');
    }
}

void solve() {
    ll k;
    string s;
    cin >> s >> k;
    ll cnt = 0;
    loop(i,sz(s) + 1 - k) {
        if(s[i] == '-') {
            revert(s,i,k);
            ++cnt;
        }
    }
    ll er = 0;
    loop(i,k) {
        if(s[sz(s) + 1 - k + i] == '-') {
            er = 1;
            break;
        }
    }
    if(er == 0) {
        cout << cnt << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main () {
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ll t;
    cin >> t;
    loop(i,t) {
    cout << "Case #" << i+1 << ": ";
    solve();
    }
    return 0;
}