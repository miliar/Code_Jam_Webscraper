#define FNAME ""

#include <bits/stdc++.h>

#define hash padjf9srpi
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for (int i = 0; i < (n); i++)
#define fornr(i, n) for (int i = (n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (a); i < (b); i++)
#define gcd __gcd
#define all(a) (a).begin(), (a).end()
 
#ifdef _WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;                                                                                                                                                                                      
typedef vector <int> vi;

template <class T> T sqr(const T &a) {return a * a;}

const int MAXN = 105 * 105 * 105 + 100;
int d[MAXN][5];

int ppp[5], cnt[5], curCnt[5];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif

    int T;
    scanf("%d", &T);
    ppp[0] = 1;
    forab(i, 1, 5) ppp[i] = ppp[i - 1] * 101;
    forn(tNum, T) {
        int n, p;
        scanf("%d%d", &n, &p);
        forn(i, p) cnt[i] = 0;
        forn(i, n) {
            int x;
            scanf("%d", &x);
            cnt[x % p]++;
        }
        forn(i, MAXN) forn(j, p) d[i][j] = 0;
        forn(i, MAXN) {
            int x = i;
            forab(j, 1, p) {
                curCnt[j] = x % 101;
                x /= 101;
            }
            if (x) continue;
            forn(j, p) {
                forab(k, 1, p) {
                    int newI = i;
                    if (curCnt[k] < cnt[k]) {
                        newI += ppp[k - 1];
                        if (newI >= MAXN) cerr << MAXN << " " << i << " " << newI << " " << curCnt[k] << " " << cnt[k] << " " << k << endl;
                        assert(newI < MAXN);
                        int newJ = (j - k + p) % p;
                        d[newI][newJ ] =max(d[newI][newJ], d[i][j] + (j==0));
                    }
                }
            }
        }
        int mask = 0;
        forab(j, 1, p) {
            mask += ppp[j - 1] * cnt[j];
        } 
        int ans = 0;
        forn(j, p) ans = max(ans, d[mask][j]);
        printf("Case #%d: %d\n", tNum + 1, cnt[0] + ans);
        fflush(stdout);
    }
}


