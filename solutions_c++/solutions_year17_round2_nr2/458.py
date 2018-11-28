#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1123456;
const int mod = 1e9 + 7;
const int inf = 1e14 + 7;
int read()
{
    int x;
    scanf("%I64d", &x);
    return x;
}
int e[N];
int s[N];
char d[N];
void solve(int test)
{
    cout << "Case #" << test << ": ";
    int n, m, i, j;
    cin >> n;
    d[1] = 'R';
    d[2] = 'O';
    d[3] = 'Y';
    d[4] = 'G';
    d[5] = 'B';
    d[6] = 'V';
    int w = 0;
    for(i = 1; i <= 6; i ++)
    {
        cin >> s[i];
        w = max(w, s[i]);
    }
    if(w > n / 2)
    {
        cout << "IMPOSSIBLE" << endl;
        return ;
    }
    string ans;
    while(1)
    {
        int id = 0;
        for(int j = 1; j <= 6; j ++)
        {
            if(s[j] > s[id])
                id = j;
        }
        if(s[id] == 0)
            break;
        ans += d[id];
        s[id] --;
        int ind = 0;
        for(int j = 1; j <= n; j ++)
        {
            if(s[j] > s[ind] && id != j)
                ind = j;
        }
        if(ind != 0)
        {
            ans += d[ind];
            s[ind] --;
        }
    }
    if(ans[0] == ans[n - 1] && n != 1)
    {
        swap(ans[n - 1], ans[n - 2]);
    }
    cout << ans << endl;
}
main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++)
    {
        solve(i);
    }
}

