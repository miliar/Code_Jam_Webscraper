#include <bits/stdc++.h>

using namespace std;

#define ll long long

vector<ll> f(ll k)
{
    vector<ll> V;
    while(k != 0){
        ll x = k % 2;
        V.push_back(x);
        k = k/2;
    }
    reverse(V.begin(), V.end());
    return V;
}

int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int cases, caseno = 0;
    scanf("%d", &cases);
    while(cases--){
        ll n, k;
        scanf("%lld %lld", &n, &k);
        vector<ll> V = f(k);
        for(int i=V.size()-1; i>0; i--){
            n = (n - V[i])/2;
        }
        ll a, b;
        if(n % 2 == 0){
            a = n/2;
            b = n/2 - 1;
            if(b < 0) b = 0;
        }
        else {
            a = (n-1)/2;
            if(a < 0) a = 0;
            b = a;
        }
        cout << "Case #" << ++caseno << ": " << max(a, b) << " " << min(a, b) << endl;
    }
}
