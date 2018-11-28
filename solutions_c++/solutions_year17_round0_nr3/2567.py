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

void ex(int num, ll ans)
{
    cout << "Case #" << num << ": " << ans / 2 << " " << (ans - 1) / 2 << "\n";
}

void solve(int num, ll n, ll k)
{
    set <pair <ll, ll>> st;
    st.insert({-n, 1});
    map <ll, ll> cnt;
    cnt[-n] = 1;
    ll ans = 0;
    
    while (k)
    {
        auto t = *st.begin();
        st.erase(st.begin());
        if (t.second < k)
        {
            k -= t.second;    
            pair <ll, ll> old1 = {(t.first + 1) / 2, cnt[(t.first + 1) / 2]};
            pair <ll, ll> old2 = {(t.first) / 2, cnt[(t.first) / 2]};
            st.erase(old1);
            st.erase(old2);
            cnt[(t.first + 1) / 2] += t.second;
            cnt[(t.first) / 2] += t.second;
            st.insert({(t.first + 1) / 2, cnt[(t.first + 1) / 2]});
            st.insert({(t.first) / 2, cnt[(t.first) / 2]});   
            //cout << (t.first + 1) / 2 << " " << (t.first) / 2 << "\n";
        }
        else
        {
            k = 0;
            ans = -t.first;
            //cout << ans << "\n";
        }
    } 

    ex(num, ans);
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
        ll n, k;
        cin >> n >> k;
        solve(i, n, k);
    }

    return 0;
}