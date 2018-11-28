#include <bits/stdc++.h>
using namespace  std;

#define bits(a)     __builtin_popcount(a)

#define PB          push_back
#define SIZE(x)     (int)x.size()
#define MP(x,y)     make_pair(x,y)
#define All(t)      (t).begin(),(t).end()
#define CLR(x,y)    memset(x,y,sizeof(x))
#define FOR(i,n,m)  for (int i = n; i <= m; i++)
#define ROF(i,n,m)  for (int i = n; i >= m; i--)

#define RI(x)       scanf ("%d", &(x))
#define RII(x,y)    RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)

typedef long long ll;
typedef unsigned int ui;
typedef unsigned long long ull;

/***********************END OF DEFINE******************************/

const int mx = 55;

int t, n, p;
int c[mx], s[mx], q[mx][mx];

void solve() {
    int ret = 0;
    for (int i = 1; i <= n; i++) s[i] = 1;
    for (int ss = 1; ss <= 1000000; ss++) {
        bool flag = true;
        for (int i = 1; i <= n; i++) {
            ll d = ceil(ss * c[i] * 0.9);
            while (s[i] <= p && q[i][s[i]] < d)
                s[i] ++;
            d = floor(ss * c[i] * 1.1);
            if (q[i][s[i]] > d || s[i] > p)
                flag = false;

        }
        if (flag) {
            ret ++;
            ss --;
            for (int i = 1; i <= n; i++)
                s[i] ++;
        }
        flag = false;
        for (int i = 1; i <= n; i++)
            if (s[i] > p)
                flag = true;
        if (flag)
            break;
    }
    cout << ret << endl;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);

    cin >> t;
    for (int cs = 1; cs <= t; cs ++){
        cin >> n >> p;
        for (int i = 1; i <= n; i++) cin >> c[i];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= p; j++) {
                cin >> q[i][j];
            }
            sort(q[i] + 1, q[i] + p + 1);
        }
        cout << "Case #" << cs << ": ";
        solve();
    }
    return 0;
}
