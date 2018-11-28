#include <bits/stdc++.h>

#define st first
#define nd second
#define pb push_back
#define mp make_pair

#define cl(x,y) memset(x, y, sizeof(x))
#define dbs(x) cerr << x << endl;
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f, MOD = 1e9+7;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const double PI=acos(-1), EPS = 1e-9;
const int N = 1e5+9;

int main () {
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        int d,n;
        scanf("%d %d", &d, &n);
        double s = 0;
        for(int i = 0; i < n; i++) {
            int k,v;
            scanf("%d %d", &k, &v);
            s = max(s, double(d-k)/v);
        }
        printf("Case #%d: %.10lf\n", t, d/s);
    }

    return 0;
}
