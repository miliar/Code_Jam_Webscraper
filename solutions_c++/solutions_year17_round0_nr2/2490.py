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

void ex(int num, string ans)
{
    if (ans[0] == '0')
        ans.erase(0, 1);
    cout << "Case #" << num << ": " << ans << "\n";
}

bool check(string s)
{
    if (s.size() == 1)
        return 1;
    for (int i = 0; i < s.size() - 1; i++)
        if (s[i] > s[i + 1])
            return 0;
    return 1;
}

void solve(int num, string n)
{
    int d = n.size();
    while (!check(n))
    {
        for (int j = 0; j < d - 1; j++)
            if (n[j] > n[j + 1])
            {
                n[j]--;
                j++;
                for (j; j < d; j++)
                    n[j] = '9';
            }
    }
    ex(num, n);
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
        string n;
        cin >> n;
        solve(i, n);
    }

    return 0;
}