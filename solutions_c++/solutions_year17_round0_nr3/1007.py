#include <iostream>
using namespace std;
typedef long long ll;

int T;

pair<ll, ll> go(ll N, ll K)
{
    if (K == 1)
        return make_pair(N/2, (N - 1)/2);
    if (N % 2 == 1)
        return go(N/2, K/2);
    else
    {
        if (K % 2 == 1)
            return go((N - 1)/2, K/2);
        return go(N/2, K/2);
    }
}

int main()
{
    ios::sync_with_stdio(0);

    freopen("Cin.txt", "r", stdin); 
    freopen("Cout.txt", "w", stdout); 

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        ll N, K;
        cin >> N >> K;
        pair<ll, ll> ans = go(N, K);
        cout << "Case #" << t << ": " << ans.first << " " << ans.second << "\n";
    }

    return 0;
}
