// from https://stackoverflow.com/questions/1830158/how-to-call-erase-with-a-reverse-iterator
#include <iostream>
#include <stdio.h>
#include <map>

typedef long long ll;
typedef float flt;

using namespace std;

ll divup(ll a, ll b)
{
    return (a + b - 1) / b;
}

void solve(int test_number)
{
    ll n, k;
    cin >> n >> k;
    
    map<ll, ll> mp;
    mp[n] = 1;
    while (true)
    {
        auto iter = mp.rbegin();
        ll len = iter->first, cnt = iter->second;
        mp.erase( --(iter.base()) );
        
        --len;
        ll s1 = len / 2, s2 = divup(len, 2);
        // cout << s1 << ' ' << s2 << endl;
        if (cnt >= k)
        {
            cout << "Case #" << test_number << ": " << 
                max(s1, s2) << ' ' << min(s1, s2) << endl;
            break;
        }
        k -= cnt;
        mp[s1] += cnt;
        mp[s2] += cnt;
    }
}

int main()
{
//  /*
    freopen("ctest.in", "r", stdin);
    freopen("ctest.out", "w", stdout);
//  */
    
    int cnt_tests;
    cin >> cnt_tests;
    for (int q = 0; q < cnt_tests; ++q)
    {
        solve(q + 1);
    }
    
    
    return 0;
}
