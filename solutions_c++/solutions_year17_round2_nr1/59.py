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
const ld eps = 1e-9;
const int INF = (int)1e9;
const int MAXN = 1111;

int T, n, tmp, x, y;
ld D;
ld pos[MAXN], v[MAXN];    

bool ok(ld v0) {
    ld t = D / v0;
    forn(i, n) {
        ld dx = pos[i];
        if (v0 - v[i] > 0) {
            ld dt = dx / (v0 - v[i]);
            if (t >= dt) {
                return 0;                   
            }
        }
    }
    
    return 1;
}

int main() {

    cout.precision(30);
    
    cin >> T;
    forn(ttt, T) {
        printf("Case #%d: ", ttt + 1);

        cin >> tmp >> n;
        D = tmp;
        forn(i, n) {
            scanf("%d%d", &x, &y);
            pos[i] = x;
            v[i] = y;    
        }
        
        ld L = 0, R = (ld)1e30;
        ld mid;
        forn(ii, 200) {
            mid = (L + R) / 2;
            if (ok(mid)) {
                L = mid;
            } else {
                R = mid;   
            }
        }
        
        cout << R;
        cout << '\n';   
    }
    
    return 0;
}