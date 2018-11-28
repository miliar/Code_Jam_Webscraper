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

int main(){
    ios::sync_with_stdio(false), cin.tie(0);

    int t; cin >> t;

    for (int i=0; i<t; i++) {
        dbn(i);
        int n, k; cin >> n >> k;

        multiset<int> diff;
        diff.insert(n);

        for (int j=0; j<k-1; j++) {
            int kk = *diff.rbegin();
            diff.erase(--diff.end());

            // dbn(kk);

            if (kk % 2) {
                diff.insert(kk/2);
                diff.insert(kk/2);
            } else {
                diff.insert(max(0, (kk/2) - 1));
                diff.insert(kk/2);
            }
        }

        int kk = *diff.rbegin();
        diff.erase(--diff.end());

        // dbn(kk);

        cout << "Case #" << i+1 << ": ";
        if (kk % 2) {
            diff.insert(kk/2);
            diff.insert(kk/2);

            // dbn(kk/2);

            cout << kk/2 << " " << kk/2 << endl;
        } else {
            int a = max(0, (kk/2) - 1);
            int b = kk/2;

            diff.insert(a);
            diff.insert(b);

            cout << max(a,b) << " " << min(a,b) << endl;
        }
    }
}