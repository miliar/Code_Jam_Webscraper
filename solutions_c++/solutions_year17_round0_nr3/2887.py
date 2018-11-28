#include <bits/stdc++.h>
#define ll long long
#define pii pair<ll, ll>
#define piii pair<pair<ll, ll>, ll>
#define A first
#define B second
#define mp make_pair
using namespace std;
void go(int cnum)
{
    ll n, k;
    cin >> n >> k;
    cout << "Case #" << cnum << ": ";
    map<pii, ll> v;
    v[mp((n-1)/2, n/2)] = 1;
    while(v.size())
    {
        pii t = v.rbegin()->A;
        ll occ = v.rbegin()->B;
        v.erase(v.rbegin()->A);
        k -= occ;
        v[mp((t.A-1)/2, t.A/2)] += occ;
        v[mp((t.B-1)/2, t.B/2)] += occ;
        if(k <= 0)
        {
            cout << t.B << " " << t.A << "\n";
            return;
        }
    }
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i=1; i<=t; i++)
        go(i);
    return 0;
}
