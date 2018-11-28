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
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define debug(args...) {vector<string> _v = split(#args, ','); err(_v.begin(), args); puts("");}
vector<string> split(const string& s, char c) {vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.emplace_back(x); return move(v);}
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) {cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", "; err(++it, args...);}

#define pb push_back
#define mp make_pair
#define all(x)  (x).begin(),(x).end()
#define tr(c, it)   for(auto it=c.begin(); it!=c.end(); it++)
#define clr(a, b)   memset(a, b, sizeof(a))

const int N = 10010;
char str[N];
int len;
int d;

const int mod = 1000000007;
LL dp[N][100];

LL dfs(int pos, int s, bool flag)
{
    if(flag == false && dp[pos][s] != -1)
        return dp[pos][s];

    if(pos == len + 1) return s == 0;

    LL ans = 0;
    int lim = flag ? str[pos] - '0' : 9;

    for(int i=0; i<=lim; i++)
    {
        ans += dfs(pos+1, (s + i) % d, flag && i == lim);
        ans %= mod;
    }

    if(flag == false)
        dp[pos][s] = ans;

    return ans;
}


int main()
{
#ifdef LOCAL
    freopen("in", "r", stdin);
    //freopen("out", "w", stdout);
#endif

    while(~scanf("%d%s", &d, str+1))
    {
        clr(dp, -1);
        len = strlen(str + 1);
        int ans = dfs(1, 0, 1);
        ans = (ans - 1 + mod) % mod;
        printf("%d\n", ans);
    }

    return 0;
}
