#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <set>
#include <string>
using namespace std;
typedef long long ll;

#define MOD 1000000007ll
#define oo 1000000007ll
#define PI 3.141592653589793238462643
#define MAXN 30
#define TT 61

ll gcd(ll a,ll b){
    if(!a) return b;
    return gcd(b%a, a);
}
pair<ll, ll> extended_gcd(ll a, ll b) {
    if (b == 0) return make_pair(1, 0);
    pair<ll, ll> t = extended_gcd(b, a % b);
    return make_pair(t.second, t.first - t.second * (a / b));
}
ll modinverse(ll a, ll m) {
    return (extended_gcd(a, m).first % m + m) % m;
}

ll fact[2020];

ll combi(ll N, ll M){
    ll res = 1;
    for(ll i=N;i>N-M;i--){
        res *= i;
        res %= MOD;
    }
    res *= modinverse(fact[M],MOD);
    res %= MOD;
    return res;
}

int main(){
    
    int T;
    
    
    freopen("/Users/thedream/Desktop/cpp/cpp/input","r",stdin);
    freopen("/Users/thedream/Desktop/cpp/cpp/output","w",stdout);
    
    scanf("%d",&T);
    
    for(int t=1;t<=T;t++){
        string a;
        int k;
        cin >> a >> k;
        int n = a.length();
        int ans = 0;
        for(int i=k;i<=n;i++){
            if(a[i-k] == '-') {
                for(int j=i-k;j<i;j++) {
                    if(a[j] == '+') a[j] = '-';
                    else a[j] = '+';
                    
                }
                ans ++;
            }
        }
        for(int i=0;i<n;i++){
            if(a[i] == '-') ans = -1;
        }
        
        printf("Case #%d: ",t);
        if(ans>=0) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
    
    
    return 0;
}

