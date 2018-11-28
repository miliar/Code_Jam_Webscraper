#include <bits/stdc++.h>

#define dout2(x) cerr << #x << " = "<< (x) << "\n";

using namespace std;

typedef long long ll;
typedef long double ld;

void dout() 
{
    cerr << "\n";
}

template <typename Head, typename... Tail>
void dout(Head H, Tail... T)
{
    cerr << H << " ";
    dout(T...);
}

void ex(int num, int ans = 0, bool ok = 0)
{
    if (ok)
        cout << "Case #" << num << ": " << ans << "\n";
    else
        cout << "Case #" << num << ": IMPOSSIBLE\n"; 
}

void solve(int num, string s, int k)
{
    int ans = 0;
    int n = s.size();
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '-')
        {
            for (int j = i; j < i + k; j++)
            {
                if (j == n)
                {
                    ex(num);
                    return;
                }
                s[j] = (s[j] == '+' ? '-' : '+');
            }
            ans++;
        }
    }
    ex(num, ans, 1);
}

signed main()
{
#ifdef PC
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        string s;
        int k;
        cin >> s >> k;   
        solve(i, s, k);
    }

    return 0;
}