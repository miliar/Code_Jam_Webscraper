#include <bits/stdc++.h>
#define pb push_back
#define f first
#define s second
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
using namespace std;
ll n;
ll rep(ll dig, ll pw)
{
    ll ret = 0;
    for(int i = 0; i < pw; i++)ret = 10*ret + dig;
    return ret;
}
ll _main()
{
    ll ret = 0, pw = 1, sz;
    cin >> n;
    string str = to_string(n);
    sz = str.size();
    for(int i = 0; i < sz-1; i++)pw *= 10;
    if(rep(1, sz) <= n)
    {
        for(int i = 0; i < sz; i++)
        {
            for(int d = 9; d >= 1; d--)if(ret + rep(d, sz-i) <= n)
            {
                ret += d * pw;
                pw /= 10;
                break;
            }
        }
        return ret;
    }
    else
    {
        return rep(9, sz-1);
    }
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
        cout << "Case #" << i << ": " << _main() << "\n";
    }
    return 0;
}
