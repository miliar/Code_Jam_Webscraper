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

const int MAXN = 1e5 + 100;

char s[MAXN];
int toFlip[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);

    int T;
    scanf("%d", &T);
    forn(tNum, T) {             
        int k;
        scanf(" %s%d", s, &k);
        int n = strlen(s);
        int ans = 0;
        int flag = 0;
        forn(i, n) toFlip[i] = 0;
        forn(i, n - k + 1) {
            flag ^= toFlip[i];
            if (flag)
                s[i] = s[i] == '-' ? '+' : '-';
            if (s[i] == '-') flag ^= 1, toFlip[i + k] = 1, ans++;
        }
         
        forab(i, n - k + 1, n) {
            flag ^= toFlip[i];
            if (s[i] == '-' && !flag) ans = -1;
            if (s[i] == '+' && flag) ans = -1;
        }
        printf("Case #%d: ", tNum + 1);
        if (ans == -1) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
}

