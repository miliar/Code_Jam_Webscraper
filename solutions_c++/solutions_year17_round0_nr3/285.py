#include <bits/stdc++.h>

using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ll big = 1000000007ll;
ll big2 = 1000000009ll;
ll n,m,q,T,k;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("autput.txt","w",stdout);

    cin >> T;
    for(ll c4 = 0; c4 < T; c4++){
        cin >> n >> k;
        ll t = 1;
        while(t <= k)t *= 2;
        t /= 2;
        ll a = (n-t+1)/t + ((n-t+1)%t >= k-t+1) - 1;
        cout << "Case #" << c4+1 << ": " << a/2+a%2 << " " << a/2 << "\n";
    }


    return 0;
}
