#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cstdlib>
#include<string>
#include<bitset>
#include<iomanip>
#include<deque>
#include<utility>
#include<functional>
#include<sstream>
#define INF 1000000000
#define fi first
#define se second
#define N 1005
#define P 1000000007
#define debug(x) cerr<<#x<<"="<<x<<endl
#define MP(x,y) make_pair(x,y)
using namespace std;
typedef long long LL;
typedef pair<LL, LL> pii;
const double pi = acos(-1.0);
int n, k;
//int r[N], d[N];
pii pan[N];
double s[N];
int main()
{
    int T, i, j;
    freopen("Alarge.in", "r", stdin);
    freopen("Alarge.out", "w", stdout);
    cin >> T;
    double ans;
    int test = 0;
    while (T--)
    {
        ans = -1;
        cin >> n >> k;
        for (i = 1; i <= n; i++)
        {
            scanf("%I64d%I64d", &pan[i].se, &pan[i].fi);
            s[i] = pan[i].first * 2 * pan[i].se * pi;
        }
            //sort(pan + 1, pan + 1 + n);
        
        if (n == k)
            debug(test);
        if (test == 15)
        {
            debug(n);
            debug(k);
        }
        for (i = 1; i <= n; i++)
        {
            //debug(i);
            priority_queue<double, vector<double>, greater<double> > q;
            for (j = 1; j <= n; j++)
                if (j != i && pan[j].se <= pan[i].se && k!=1)
                {
                    if (q.size() == k - 1)
                    {
                        if (q.top() < s[j])
                            q.pop(), q.push(s[j]);
                    }
                    else
                        q.push(s[j]);
                }
            if (test == 15)
                debug(q.size());
            if (q.size() == k - 1)
            {
                double now = s[i] + pi*pan[i].se*pan[i].se;
                while (!q.empty())
                    now += q.top(), q.pop();
                //debug(i);
                //debug(he);
                //debug(he*pi * 2 * pan[i].se + pi*pan[i].se*pan[i].se);
                //debug(he*pi * 2 * pan[i].se);
                //debug(pi*pan[i].se*pan[i].se);
                if (test == 15)
                    debug(now);
                ans = max(ans, now);
            }
        }
        test++;
        printf("Case #%d: %.9f\n", test, ans);
        if (ans == -1)
            debug(n);
        //cout << ans << endl;
    }
}
// davidlee1999WTK 2017/
// ios::sync_with_stdio(false);
//#pragma comment(linker, "/STACK:102400000,102400000") compiler c++,not g++
/*

*/
