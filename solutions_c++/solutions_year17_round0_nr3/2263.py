#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main(){

    int t;
    scanf ("%d", &t);
    for (int cc = 1; cc <= t; cc++){
        ll n, k;
        cin >> n >> k;
        map <ll, ll> qtd;
        set <ll> s;
        qtd[n]++;
        s.insert (n);
        while (true){
            ll num = *s.rbegin();
            s.erase(*s.rbegin());
            ll q = qtd[num];
            if (q >= k){
                printf ("Case #%d: %lld %lld\n", cc, num/2,  (num-1) / 2);
                break;
            }
            s.insert ((num-1)/2);
            s.insert (num/2);
            qtd[(num-1)/2] += q;
            qtd[num/2] += q;
            k -= q;
        }
    }

    return 0;
}
