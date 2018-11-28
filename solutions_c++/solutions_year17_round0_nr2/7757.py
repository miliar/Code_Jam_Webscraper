#include <bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair
#define var(x) cerr << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

ll solve(ll k) {
    ll v = 0;
    ll p = 1;
    while(k) {
        ll x = k%10;
        ll y = (k/10)%10;
        if(x < y && k > 9) {
            k -= (x+1);
            while(p != 1) {
                k *= 10;
                k += 9;
                p /= 10;
            }
            return solve(k);
        } else {
            v += p*x;
            p *= 10;
            k /= 10;
        }
    }
    return v;
}

int main() {
    int N;
    cin >> N;
    for(int n=1;n<=N;n++) {
        ll k;
        cin >> k;
        printf("Case #%d: %lld\n", n, solve(k));
    }
    return 0;
}

