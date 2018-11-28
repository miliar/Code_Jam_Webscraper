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



void solve() {
    ld d;
    ll n;
    cin >> d >> n;
    ld maxt = 0;
    ll init = 0;
    ld pos, vmax;
    ld curt;
    loop(i,n) {
        cin >> pos >> vmax;
        curt = (d - pos)/vmax;
        if(init == 0 || curt > maxt) {
            init = 1;
            maxt = curt;
        }
    }

    cout<<fixed;
    cout.precision(12);
    cout << d/maxt << endl;
}

int main () {
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ll t;
    cin >> t;
    loop(i,t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;


}
