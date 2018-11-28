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

set<ll> S;
void gena(ll i){
if(i > 1000000000000000000)return;
S.insert(-i);
ll im = i%10;
for(ll c1 = im; c1 < 10; c1++){
    gena(i*10+c1);
}
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("autput.txt","w",stdout);

    cin >> T;

    for(ll c1 = 1; c1 < 10; c1++)gena(c1);
    for(ll c4 = 0; c4 < T; c4++){
        cin >> n;
        cout <<"Case #" << c4+1 << ": " << -*S.lower_bound(-n) << "\n";
    }


    return 0;
}
