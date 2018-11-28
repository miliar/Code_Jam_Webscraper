#include<bits/stdc++.h>
using namespace std;
#define ll long long
vector<int> v;
void makeArr(ll x)
{
    v.clear();
    while(x)
    {
        v.push_back(x%10);
        x /= 10;
    }
    reverse(v.begin(), v.end());
}

ll dp(int curr, int smaller, int lastdigit, int m, ll num)
{
    if(curr == m)
    {
        return num;
    }
    ll ans = -1;
    if(smaller)
    {
        for(int i = lastdigit; i <= 9; i++)
        {
            ans = max(ans, dp(curr + 1, 1, i, m, num*10+i));
        }
    }
    else
    {
        for(int i = lastdigit; i <= v[curr]; i++)
        {
            if(i < v[curr]) ans = max(ans, dp(curr + 1, 1, i, m, num*10+i));
            else ans = max(ans, dp(curr + 1, 0, i, m, num*10+i));
        }
    }
    return ans;
}

int main()
{

   // freopen("intput.txt","r", stdin);
    freopen("output.out", "w", stdout);

    int t;
    ll n;
    scanf("%d",&t);
    for(int tc = 1; tc <= t; tc++)
    {
        scanf("%lld",&n);
        makeArr(n);
        ll ans = dp(0, 0, 0, v.size(), 0);
        printf("Case #%d: %lld\n",tc, ans);

    }
}
