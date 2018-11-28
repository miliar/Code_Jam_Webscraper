#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define f first
#define sec second
#define fro for
#define itn int
#define pb push_back
#define pii pair<int,int>
#define pll pair<ll,ll>

int n, k, ans;
string s, s1;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> s >> k;
        s1.clear();
        ans = 0;
        for (int j = 0; j < s.size(); j++) s1 += "+";

        for (int j = s.size() - 1; j >= k - 1; j--)
        {
            if (s[j] == '-')
            {
                for (int j1 = j; j1 >= j - k + 1; j1--)
                {
                    if (s[j1] == '-') s[j1] = '+';
                    else s[j1] = '-';
                }
                ans++;
            }
        }
        if (s == s1) cout << "Case #" << i + 1 << ": " << ans << endl;
        else cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }

    return 0;
}
