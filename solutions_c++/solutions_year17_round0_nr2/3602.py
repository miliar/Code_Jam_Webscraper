#include <bits/stdc++.h>

#define ll long long
using namespace std;
ifstream f("d.in");
ofstream g("d.out");

const ll NMax = 10001;

ll t,nr,n;
ll v[NMax];

int main()
{
    f >> t;
    for(ll co = 1; co <= t; ++co){
        f >> n;

        ///daca nu incepe cu 1
        ll x = n;
        nr = 0;
        while(x){
            ll c = x % 10;
            v[++nr] = c;
            x /= 10;
        }

        for(ll i = 1; i < nr; ++i){
            if(v[i] < v[i + 1]){
                v[i + 1]--;
                for(ll j = 1; j <= i; ++j){
                    v[j] = 9;
                }
            }
        }

        if(v[nr] == 0)
            nr--;
        g << "Case #" << co << ": ";
        for(ll i = nr; i >= 1; --i){
            g << v[i];
        }
        g << '\n';
    }
    return 0;
}
