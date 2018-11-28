#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-8;
const int INF = (int)1e9;
const int MAXN = 1111;

int T;
int n, m, c;
int deg[MAXN], cnt[MAXN], rest[MAXN];
vi needs;
pii ans;

bool ok(int sz) {
    ans = {sz, 0};
    needs.clear();
    forn(i, MAXN) {
        if (cnt[i] <= sz) {
            rest[i] = sz - cnt[i];   
        } else {
            rest[i] = 0;
            forn(j, cnt[i] - sz) {
                needs.pb(i);   
            }
            ans.Y += cnt[i] - sz;
        }
    }
/*    
    cout << "nds:\n";
    for (auto x: needs) {
        cout << x << ' ';
    }
    cout << "cnts:\n";
    forn(i, 10) {
        cout << rest[i] << ' ';
    }
    cout << '\n';
*/    
    int ptrn, pos;
    for (ptrn = 0, pos = 0; ptrn < (int)needs.size() && pos < MAXN; ) {
        if (needs[ptrn] <= pos) {
            return 0;
        }
        if (rest[pos] == 0) {
            pos++;
            continue;
        }
        rest[pos]--;
        ptrn++;
    }
    
    return 1;
}

int main() {
        
    cin >> T;
    forn(tt, T) {
        printf("Case #%d: ", tt + 1);
        
        memset(deg, 0, sizeof(deg));
        memset(cnt, 0, sizeof(cnt));
        
        scanf("%d%d%d", &n, &c, &m);
        
        forn(i, m) {
            int x, id;
            scanf("%d%d", &x, &id);
            x--, id--;    
            assert(0 <= id && id < c);
            assert(0 <= x && x < n);
            
            cnt[x]++;
            deg[id]++;
        }
        
        int maxDeg = 0;
        forn(i, c) {
            maxDeg = max(maxDeg, deg[i]);    
        }
        
       // cout << ok(1) << '\n';
        
        int L = maxDeg - 1, R = MAXN - 1, mid;
        while (R - L > 1) {
            mid = (L + R) / 2;
            if (ok(mid)) {
                R = mid;
            } else {
                L = mid;   
            }
        }
        assert(ok(R));
        
        printf("%d %d\n", ans.X, ans.Y);
    }
    
    return 0;
}
