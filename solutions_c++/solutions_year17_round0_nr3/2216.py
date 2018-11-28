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

#define MAXN 1000100

int GI(int &a){return scanf("%I64d", &a);}

int n, i, j, k, tmp, m, x, b, t, d;
int a;
int next[MAXN];
int prev[MAXN];
vi v1, v2, v3;

int32_t main(){
    freopen("c3.in", "rt", stdin);
    freopen("c3.out", "wt", stdout);
    cin >> t;
    map<int, int>::iterator it;
    REP(z, t){
        cin >> n >> k;
        map<int, int> mm;
        mm[n] = 1;
        int remain = k - 1;
        while (remain > 0){
            int num = mm.rbegin()->first;
            int cur = mm.rbegin()->second;
            if (cur <= remain){
                remain -= cur;

                it = mm.end();
                it--;
                mm.erase(it);

                mm[num / 2] += cur;
                mm[num / 2 - 1 + num % 2] += cur;
            } else {
                mm.rbegin()->second -= remain;
                remain = 0;
            }
        }
        a = mm.rbegin()->first;

        cout << "Case #" << z + 1 << ": " << a/2 << " " << a/ 2 - 1 + a % 2 << "\n";
    }
}
