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

int T;
int n, m;
char g[55][55];

int beam_val[55][55];

vector<PII> beam;


int main()
{
#ifdef LOCAL
    //freopen("in", "r", stdin);
    //freopen("B-small-attempt0.in.txt", "r", stdin);
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-large.in", "r", stdin);
    //freopen("out", "w", stdout);
#endif

    int cas = 1;
    scanf("%d", &T);

    while(T--)
    {
        printf("Case #%d: ", cas++);

        scanf("%d%d",&n, &m);
        for(int i=1; i<=n; i++)
            scanf("%s", g[i] + 1);

        beam.clear();
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                if(g[i][j] == '-' || g[i][j] == '|')
                {
                    g[i][j] = '+';
                    beam.push_back({i,j});
                    beam_val[i][j] = 3;

                }

            }
        }


        bool can = true;


        tr(beam, i)
        {
            int r1 = i.first;
            int c1 = i.second;

            tr(beam, j)
            {
                int r2 = j.first;
                int c2 = j.second;

                if(r1 == r2)
                {

                    bool ok = false;
                    for(int k=min(c1, c2)+1; k<max(c1, c2); k++)
                        if(g[r1][k] == '#')
                            ok = true;
                    if(ok == false)
                    {
                        if(g[r1][c1] != '+' || g[r1][c2] != '+')
                        {
                            can = false;
                            break;
                        }
                        g[r1][c1] = g[r2][c2] = '|';
                    }
                }

                if(c1 == c2)
                {

                    bool ok = false;
                    for(int k=min(r1, r2)+1; k<max(r1, r2); k++)
                        if(g[k][c1] == '#')
                            ok = true;
                    if(ok == false)
                    {
                        if(g[r1][c1] != '+' || g[r1][c2] != '+')
                        {
                            can = false;
                            break;
                        }
                        g[r1][c1] = g[r2][c2] = '-';
                    }

                }
            }
        }

        if(can == false)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }





    }

    return 0;
}

