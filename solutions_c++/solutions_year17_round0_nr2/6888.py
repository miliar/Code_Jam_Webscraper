#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 11234;
const int mod = 1e9 + 7;
const int inf = 1e9 + 7;
int read()
{
    int x;
    scanf("%I64d", &x);
    return x;
}
void solve(int x)
{
    string s;
    cin >> s;
    int t = 1;
    for(int i = 0; i < s.size(); i ++)
    {
        if(t > s[i] - 48)
        {
            t = i - 1;
            while(t >= 0 && s[t] > s[t + 1])
            {
                s[t] --;
                t --;
            }
            for(int j = t + 2; j < s.size(); j ++)
                s[j] = '9';
            break;
        }
        t = max(t, (s[i] - 48) * 1ll);
    }
    while(s[0] == '0')
    {
        s = s.substr(1);
    }
    cout << "Case #" << x << ": ";
    cout << s << endl;
}
main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int n, m, i, j;
    cin >> n;
    for(int i = 1; i <= n; i ++)
    {
        solve(i);
    }
}

