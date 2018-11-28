#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;

string str;
int n, k;
int _main()
{
    cin >> str >> k;
    n = str.size();
    int ans = 0;
    for(int i = 0; i <= n-k; i++)
    {
        if(str[i] == '-')
        {
            for(int j = i; j < i + k; j++)
            {
                if(str[j] == '-')str[j] = '+';
                else str[j] = '-';
            }
            ans++;
        }
    }
    for(int i = 0; i < n; i++)if(str[i] == '-')return -1;
    return ans;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    cin >> tt;
    for(int i = 1; i <= tt; i++)
    {
        int x = _main();
        if(x == -1)cout << "Case #" << i << ": IMPOSSIBLE\n";
        else cout << "Case #" << i << ": " << x << "\n";
    }
    return 0;
}
