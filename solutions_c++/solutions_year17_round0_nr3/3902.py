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

void enter(multiset<ll>& Set) {
    ll len = *(--Set.end());
    Set.erase(--Set.end());
    Set.insert((len-1)/2);
    Set.insert((len)/2);
}


void solve() {
    ll k,n;
    cin >> n >> k;
    multiset <ll> Set;

    Set.insert(n);
    loop(i,k-1) {
        enter(Set);
    }
    ll best = *(--Set.end());
    cout << (best)/2 << " " << (best-1)/2 << endl;
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