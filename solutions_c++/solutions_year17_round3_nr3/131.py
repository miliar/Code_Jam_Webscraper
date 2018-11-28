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
#define N 55
#define P 1000000007
#define debug(x) cerr<<#x<<"="<<x<<endl
#define MP(x,y) make_pair(x,y)
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;
double p[N];
int main()
{
    int T, n, i, k;
    freopen("Csmall1.in", "r", stdin);
    freopen("Csmall1.out", "w", stdout);

    cin >> T;
    int test = 0;
    while (T--)
    {
        test++;
        cin >> n >> k;
        
        double u, avr;
        cin >> u;
        for (i = 1; i <= n; i++)
            cin >> p[i];
        sort(p + 1, p + 1 + n);
        p[n + 1] = 1;
        for (i = 1; i <= n; i++)
        {
            //debug(i);
            if (p[i] < p[i + 1])
            {
                avr = min(u / i, p[i + 1] - p[i]);
                //debug(avr);
                for (int j = 1; j <= i; j++)
                {
                    p[j] += avr;
                }
                u = u - avr * i;
            }

        }
        double rel = 1;
        for (i = 1; i <= n; i++)
            rel = rel * p[i];
        printf("Case #%d: %.9f\n",test, rel);
    }
}
// davidlee1999WTK 2017/
// ios::sync_with_stdio(false);
//#pragma comment(linker, "/STACK:102400000,102400000") compiler c++,not g++
/*

*/
