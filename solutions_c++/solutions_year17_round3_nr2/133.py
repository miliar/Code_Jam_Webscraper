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
#define N 100005
#define P 1000000007
#define debug(x) cerr<<#x<<"="<<x<<endl
#define MP(x,y) make_pair(x,y)
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;
struct Per
{
    int l, r, op;
}per[N];
vector<Per> ca, ja;
vector<int> tc, tj;
bool cmp(Per a, Per b)
{
    return a.l < b.l;
}
int main()
{
    int T, i, j, nc, nj, n;
    int sum_c, sum_j;
    int ans;
    freopen("Blarge.in", "r", stdin);
    freopen("Blarge.out", "w", stdout);
    cin >> T;
    int test = 0;
    while (T--)
    {
        ans = 0;
        tc.clear();
        tj.clear();
        cin >> nc >> nj;
        sum_c = sum_j = 0;
        n = nc + nj;
        for (i = 1; i <= nc; i++)
        {
            scanf("%d%d", &per[i].l, &per[i].r);
            per[i].op = 0;
            sum_c += per[i].r - per[i].l;
            ca.push_back(per[i]);
        }
        for (i = 1; i <= nj; i++)
        {
            scanf("%d%d", &per[i+nc].l, &per[i+nc].r);
            sum_j += per[i+nc].r - per[i+nc].l;
            per[i+nc].op = 1;
            ja.push_back(per[i+nc]);
        }
        sort(per + 1, per + 1 + n, cmp);
        for (i = 1; i < n; i++)
        {
            if (per[i].op != per[i + 1].op)
                ans++;
            else
            {
                if (per[i].op == 0)
                    tc.push_back(per[i + 1].l - per[i].r);
                else
                    tj.push_back(per[i + 1].l - per[i].r);
            }
        }
        if (per[1].op != per[n].op)
            ans++;
        else
        {
            if (per[n].op == 0)
                tc.push_back(1440 - per[n].r + per[1].l);
            else
                tj.push_back(1440 - per[n].r + per[1].l);
        }
        sort(tc.begin(), tc.end());
        sort(tj.begin(), tj.end());

        for (i = 0; i < tc.size(); i++)
            if (sum_c + tc[i] <= 720)
                sum_c += tc[i];
            else break;
        ans += (tc.size() - i) * 2;

        for (i = 0; i < tj.size(); i++)
            if (sum_j + tj[i] <= 720)
                sum_j += tj[i];
            else break;
        ans += (tj.size() - i) * 2;
        test++;
        printf("Case #%d: %d\n", test, ans);
    }
}
// davidlee1999WTK 2017/
// ios::sync_with_stdio(false);
//#pragma comment(linker, "/STACK:102400000,102400000") compiler c++,not g++
/*

*/
