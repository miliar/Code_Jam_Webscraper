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

char s[20];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);

    int T;
    scanf("%d", &T);
    forn(tNum, T) {
        scanf(" %s", s);
        int len = (int) strlen(s);
        int pos = len;
        fornr(i, len - 1) {
            if (s[i] > s[i + 1]) {
                pos = i; 
            }
        }
        while (pos > 0 && s[pos - 1] == s[pos]) pos--;

        printf("Case #%d: ", tNum + 1);
        forn(i, pos) printf("%c", s[i]);
        if (pos < len && s[pos] > '1') printf("%c", s[pos] - 1);
        forab(i, pos + 1, len) printf("9");
        puts("");
    }
}

