#include <cassert>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define debug(args...) {vector<string> _v = split(#args, ','); err(_v.begin(), args); puts("");}
vector<string> split(const string& s, char c) {vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(x); return v;}
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) {cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", "; err(++it, args...);}

#if (( _WIN32 || __WIN32__ ) && __cplusplus < 201103L)
#define lld I64d
#else
#define lld lld
#endif

#define pb push_back
#define mp make_pair
#define all(x)  (x).begin(),(x).end()
#define tr(c, it)   for(auto it=c.begin(); it!=c.end(); it++)
#define clr(a, b)   memset(a, b, sizeof(a))
#define forn(i, n)   for(int i=0; i<n; i++)

const int INF = 0x3f3f3f3f;
const double eps = 1e-8;

int T;
int n, p, a[1111];
int mod[5];


int main()
{
#ifdef LOCAL
    //freopen("in", "r", stdin);
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
#endif

    int cas = 1;
    scanf("%d", &T);

    while(T--)
    {
        printf("Case #%d: ", cas++);

        scanf("%d%d", &n, &p);
        clr(mod, 0);
        for(int i=1; i<=n; i++)
        {
            scanf("%d", &a[i]);
            mod[a[i] % p] ++;

        }

        int ans = mod[0];
        if(p == 2)
        {
            ans += (mod[1] + 1) / 2;
        }
        else if(p == 3)
        {
            int c = mod[1];
            int d = mod[2];
            if(c > d) swap(c, d);
            ans += c;
            ans += (d - c + 2) / 3;

        }
        else
        {
            int c = mod[1];
            int e = mod[2];
            int d = mod[3];

            if(c > d) swap(c, d);
            ans += c;
            int left = d - c;
            ans += (e + 1) / 2;

            if(e % 2 == 1)
            {
                if(left > 2)
                {
                    left -= 2;
                    ans += (left + 3) / 4;
                }
            }
            else
            {
                ans += (left +3) / 4;

            }



        }

        printf("%d\n", ans);


    }

    return 0;
}

