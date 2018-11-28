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
typedef pair<int, int> pii;
int main()
{
    int i,T,test = 0,rel1,rel2,p,b,sum;
    int n, c, m;
    freopen("Bsmall0.in", "r", stdin);
    freopen("Bsmall0.out", "w", stdout);
    cin >> T;
    while (T--)
    {
        rel1 = rel2 = 0;
        map<int, int> mp_p,mp_man;
        cin >> n >> c >> m;
        for (i = 1; i <= m; i++)
        {
            scanf("%d%d", &p, &b);
            mp_p[p]++;
            mp_man[b]++;
        }
        sum = 0;
        for (i = 1; i <= n; i++)
        {
            sum += mp_p[i];
            rel1 = max(rel1, sum / i);
        }
        for (i = 1; i <= c; i++)
            rel1 = max(rel1, mp_man[i]);
        for (i = 1; i <= n; i++)
            if (mp_p[i] > rel1)
                rel2 += mp_p[i] - rel1;
        printf("Case #%d: ", ++test);
        cout << rel1 << ' ' << rel2 << endl;
    }
    return 0;
}
// davidlee1999WTK 2017/
// ios::sync_with_stdio(false);
//#pragma comment(linker, "/STACK:102400000,102400000") compiler c++,not g++
/*

*/
