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
const int MAXN = 500500;

int T;
string s;
int a[MAXN];
int n, k;

int main() {

    cin >> T;
    forn(tt, T) {
        printf("Case #%d: ", tt + 1);
        
        cin >> s >> k;
        n = (int)s.size();
        forn(i, n) {
            a[i] = (s[i] == '+');     
        }
        
        int ans = 0;
        for (int i = 0; i + k - 1 < n; i++) {
            if (!a[i]) {
                ans++;
                forn(j, k) {
                    a[i + j] ^= 1;   
                }
            }
        }
        
        forn(i, n) {
            if (!a[i]) {
                ans = INF;
            }
        }
        
        if (ans < INF) {
            cout << ans << '\n';
        } else {
            cout << "IMPOSSIBLE\n";   
        }
    }
    
    return 0;
}