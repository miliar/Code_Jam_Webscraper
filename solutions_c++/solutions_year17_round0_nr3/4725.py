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

multiset<int> Set;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);

        
    int T;
    scanf("%d", &T);
    forn(tNum, T) {
        int n, k;

        scanf("%d%d", &n, &k);
        Set.clear();
        Set.insert(-n);
        int lst = 0;
        forn(i, k) {
            auto x = *Set.begin();
            Set.erase(Set.begin());
            x = -x;
            x--;
            lst = x;
            if (x / 2) Set.insert(-(x / 2));
            if ((x + 1) / 2) Set.insert(-((x + 1) / 2));
//            printf("%d %d\n", (x / 2), ((x + 1) / 2));
        }
        printf("Case #%d: %d %d\n", tNum + 1, (lst + 1) / 2, lst / 2);
    }
}

