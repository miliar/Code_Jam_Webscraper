#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
#define ll long long
#define sort(A) sort(A.begin(),A.end())
#define rsort(A) sort(A.rbegin(),A.rend())
using namespace std;
static const ll D = 1000000007;

ll foo(ll n, ll k, map<ll,map<ll,ll> >& M){
    if(k==0)
        return n;
    if(M.count(n)==0)
        M[n]=map<ll,ll>();
    if(M[n].count(k)==0)
        M[n][k] = max(foo(n/2,k/2,M),foo((n-1)/2,(k-1)/2,M));
    return M[n][k];
}

int main() {
    ll T, n, k;
    cin >> T;
    for(ll t = 0; t<T; ++t){
        cin >> n >> k;
        map<ll,map<ll,ll> > M;
        ll r = foo(n,k-1,M);
        cout << "Case #" << t+1 << ": " << r/2 << " " << (r-1)/2 << endl;
    }
    return 0;
}
