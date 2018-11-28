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

string change(string s, int i, int k) {
    for (int j=i; j<i+k; j++) {
        if (s[j] == '+') {
            s[j] = '-';
        } else {
            s[j] = '+';
        }
    }

    return s;
}

string mais(int n) {
    string s = "";
    for (int i=0; i<n; i++) {
        s += '+';
    }

    return s;
}

int main(){
    ios::sync_with_stdio(false), cin.tie(0);

    int t; cin >> t;

    for (int i=0; i<t; i++) {
        string s;
        int n;
        cin >> s >> n;

        int ans = 0;
        for (int i=0; i<int(s.size()) - (n-1); i++) {
            if (s[i] == '-') {
                s = change(s,i,n);
                ans++;
            }
        }

        cout << "Case #" << i + 1 << ": ";

        if (s == mais(s.size())) {
            cout << ans << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }

    }
}  