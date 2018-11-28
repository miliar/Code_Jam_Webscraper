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
const int MAXN = 105;

int T;
int n, p;
int num[5], add;
int dp[5][MAXN][MAXN][MAXN][5];

void remax(int &x, int y) {
    x = max(x, y);    
}

int main() {

    memset(dp, 0, sizeof(dp));
    
    int sz[5];
    int nsz[5];
    for (int P = 2; P <= 4; P++) {   
        for (sz[1] = 0; sz[1] < MAXN; sz[1]++) {
            for (sz[2] = 0; sz[2] < MAXN; sz[2]++) {
                for (sz[3] = 0; sz[3] < MAXN; sz[3]++) {
                    for (int rest = 0; rest < P; rest++) { 
                        bool valid = 1;
                        bool any = 0;
                        
                        for (int i = 1; i <= 3; i++) {
                            any |= (sz[i] > 0);
                            if (i >= P && sz[i] > 0) {
                                valid = 0;   
                            }
                        }
                        
                        if (any && valid) {
                            for (int j = 1; j <= 3; j++) {
                                forn(k, 5) {
                                    nsz[k] = sz[k];
                                }
                                
                                if (sz[j] > 0) {
                                    nsz[j]--;
                                    remax(dp[P][sz[1]][sz[2]][sz[3]][rest],
                                        dp[P][nsz[1]][nsz[2]][nsz[3]][(rest + j) % P] + (rest == 0));   
                                }
                            }
                        }
                    }
                }
            }        
        }
    }
        
    cin >> T;
    forn(tt, T) {
        printf("Case #%d: ", tt + 1);
        scanf("%d%d", &n, &p);
        memset(num, 0, sizeof(num));
        forn(i, n) {
            int x;
            scanf("%d", &x);
            num[x % p]++;
        }
        
        add = num[0];
        int ans = dp[p][num[1]][num[2]][num[3]][0];
        printf("%d\n", add + ans);
    }
    
    return 0;
}
