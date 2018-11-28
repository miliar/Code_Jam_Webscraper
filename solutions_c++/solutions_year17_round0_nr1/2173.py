#include <bits/stdc++.h>
using namespace std;

#define int long long
#define ll long long
#define vi vector<int>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++i)
#define FOR(i, a, b) for (int i = (int)a, _b = b; i <= _b; ++i)
#define FORD(i, a, b) for (int i = (int)a ,_b = b; i >= _b; --i)

#define MAX(a, b) (a > b ? a : b)
#define MIN(a, b) (a < b ? a : b)

#define DEBUG(X) { cerr << #X << " = " << (X) << endl; }

#define MAXN 7100

int GI(int &a){return scanf("%I64d", &a);}

int n, i, j, k, tmp, m, x, b, t;

vi v1, v2, v3;
int a[10];

int32_t main(){
    freopen("large.in", "rt", stdin);
    freopen("large.out", "wt", stdout);
    ios_base::sync_with_stdio(false);

    string s;
    cin >> t;
	REP(z, t){
        cin >> s;
        cin >> k;
        n = s.length();
        int cur = 0;
        int dem = 0;

        while (cur + k - 1 < n){
            if (s[cur] == '-'){
                FOR(i, cur, cur + k - 1)
                    if (s[i] == '-')
                        s[i] = '+';
                    else
                        s[i] = '-';
                ++dem;
            }
            ++cur;
        }

        int ok = 1;
        REP(i, n)
            if (s[i] == '-')
                ok = 0;
        if (ok == 1)
            cout << "Case #" << z + 1 << ": " << dem << "\n";
        else
            cout << "Case #" << z + 1 << ": IMPOSSIBLE\n";
	}
}
