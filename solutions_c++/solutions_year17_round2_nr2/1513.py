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
//            0   1.  2.  3.  4.  5 
char d[6] = {'G','O','V','B','Y','R'};
string imp = "IMPOSSIBLE";
ll t[6];
ll go[6][6];

void solve() {
    go[0][5] = 1;
    go[1][3] = 1;
    go[2][4] = 1;
    go[3][1] = 1;
    go[3][4] = 1;
    go[3][5] = 1;
    go[4][2] = 1;
    go[4][3] = 1;
    go[4][5] = 1;
    go[5][0] = 1;
    go[5][3] = 1;
    go[5][4] = 1;
    ll n;
    cin >> n >>  t[5] >> t[1] >> t[4] >> t[0] >> t[3] >> t[2];
    ll cur = 3;
    ll frt;
    while(!t[cur])
        ++cur;
    frt = cur;
    vector <ll> ans;
    vector <ll> trans;
    ll er;
    while(true) {
        // cout << d[cur];
        ans.pb(cur);
        --t[cur];
        --n;
        er = 1;
        loop(i,6) {
            if(go[cur][i] > 0 && t[i] > 0 && (!(n == 1 && i == frt) || n != 1)) {
                cur = i;
                er = 0;
                break;
            }
        }

        if(er) {
            if(n != t[5]) {
                cout << imp  << endl;
                return;
            } else{ 
                ll prev;
                loop(i,sz(ans)) {
                    prev = (i - 1 + sz(ans)) % sz(ans);
                    if(n && (ans[i] == 0 || ans[i] == 3 || ans[i] == 4) 
                     && (ans[prev] == 0 || ans[prev] == 3 || ans[prev] == 4) ) {
                        trans.pb(5);
                        --t[5];
                        --n;
                    }
                    trans.pb(ans[i]);
                }
                if(n) {
                    cout << imp << endl;
                    return;
                }
                break;
            }
        }
    }
    loop(i,sz(trans)) {
        cout << d[trans[i]];
    }
    cout << endl;
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
