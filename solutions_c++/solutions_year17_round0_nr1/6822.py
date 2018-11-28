#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>


using namespace std;

#define pi acos(-1)
#define gcd(a,b) __gcd(a,b)
#define PB push_back
#define SIZE(x) (int)x.size()
#define clr(x,y) memset(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ALL(t) (t).begin(),(t).end()
#define FOR(i,n,m) for (int i = n; i <= m; i ++)
#define ROF(i,n,m) for (int i = n; i >= m; i --)
#define RI(x) scanf ("%d", &(x))
#define RII(x,y) RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)


typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;

const ll mod = 1e9+7;
const int INF = 1e9;
const double EPS = 1e-8;

/**************************************END************************************/

int t, k;
string s;

void solve()
{
    int ret = 0;
    bool flag = true;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == '-')
        {
            if (i + k > s.size())
            {
                flag = false;
                break;
            }
            ret ++;
            for (int j = 0; j < k; j++)
            {
                if (s[i + j] == '+') s[i + j] = '-';
                else s[i + j] = '+';
            }
        }
    }
    if (flag) cout << ret << endl;
    else cout << "IMPOSSIBLE" << endl;
}

int main()
{
   	freopen("/Users/apple/Desktop/A-large.in", "r", stdin);
    freopen("/Users/apple/Desktop/A-large.out", "w", stdout);
    cin >> t;
    int cas=1;
    while(t--)
    {
        for(int i=0;i<100;i++);
        cin >> s >> k;
        cout << "Case #" << cas << ": ";
        solve();
        cas++;
    }
}
