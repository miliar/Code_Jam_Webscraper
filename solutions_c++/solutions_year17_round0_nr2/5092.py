#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <ios>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <unistd.h>
#include <utility>
#include <vector>
#define dbg(args...) //fprintf(stderr, args)
#define dbc(x) cerr << x << '\n'
#define dbn(x) cerr << #x << " == " << x << '\n'
#define m(v,x) memset(v,x,sizeof(v))
#define pb push_back
#define endl '\n'
#define F first
#define S second

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

//
const int MAXM = 112345;

set<ll> tidy;

void f(int i, ll n) {
    if (n > 1000000000000000000) return;

    for (int j=i; j<=9; j++) {
        tidy.insert(10*n + j);
        f(j, 10*n + j);
    }
}

int main(){
    ios::sync_with_stdio(false), cin.tie(0);

    f(1, 0);

    int t; cin >> t;

    dbn(tidy.size());

    for (int i=0; i<t; i++) {
        ll n; cin >> n;

        set<ll>::iterator it = tidy.upper_bound(n);
        if (it != tidy.begin()) {
            cout << "Case #" << i+1 << ": " << *(--it) << endl; 
        } else {
            assert(0);
        }
    }
}