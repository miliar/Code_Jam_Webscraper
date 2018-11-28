#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARINGS
#define _USE_MATH_DEFINES

#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;

const int INF = (int)(1e9 + 1337);
const int64 LINF = (int64)(4e18);
const double EPS = (double)(1e-11);
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)(0))++)

int n, c, m;
vector<vector<int> > a;
vector<int> fr[1010];
bool u[1010][1010];
int us[1010];
int opt;

bool check(int l)
{
    for(int i = 1; i <= c; i++)
    {
        fr[i].clear();
        for(int j = 1; j <= l; j++)
            fr[i].push_back(j);
    }
    memset(u, 0, sizeof u);
    memset(us, 0, sizeof us);
    opt = 0;
    for(int i = 1; i <= n; i++)
    {
        for(int j = 0; j < (int)a[i].size();)
        {
            int ct = 0;
            int ix = a[i][j];
            while(j + ct < (int)a[i].size() && a[i][j + ct] == ix)
                ct++;

            vector<int> tv[3];
            for(int k = 0; k < (int)fr[ix].size(); k++)
            {
                int pos = fr[ix][k];
                if(!u[i][pos])
                    tv[0].push_back(pos);
                else if(us[pos] < i)
                    tv[1].push_back(pos);
                else
                    tv[2].push_back(pos);
            }
            fr[ix].clear();
            int tc = ct;
            for(int k = 0; k < (int)tv[0].size(); k++)
            {
                int pos = tv[0][k];
                if(tc == 0)
                    fr[ix].push_back(pos);
                else
                {
                    tc--;
                    u[i][pos] = 1;
                    us[pos]++;
                }
            }
            for(int k = 0; k < (int)tv[1].size(); k++)
            {
                int pos = tv[1][k];
                if(tc == 0)
                    fr[ix].push_back(pos);
                else
                {
                    tc--;
                    opt++;
                    u[i][pos] = 1;
                    us[pos]++;
                }
            }
            if(tc)
                return 0;
            for(int k = 0; k < (int)tv[2].size(); k++)
                fr[ix].push_back(tv[2][k]);
            j += ct;
        }
    }
    return 1;
}

int cur[1010];

void solve()
{
    cin >> n >> c >> m;
    a.assign(n + 1, vector<int>());
    for(int i = 0; i < m; i++)
    {
        int ix, p;
        cin >> p >> ix;
        a[p].push_back(ix);
    }
    for(int i = 1; i <= n; i++)
        sort(a[i].begin(), a[i].end());

    int l = 0, r = m, res = m;
    while(l <= r)
    {
        int mid = (l + r) >> 1;
        if(check(mid))
        {
            res = mid;
            r = mid - 1;
        }
        else
            l = mid + 1;
    }
    check(res);
    cout << res << ' ' << opt;
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
    
    int ts;
    cin >> ts;
    for(int i = 1; i <= ts; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
}



