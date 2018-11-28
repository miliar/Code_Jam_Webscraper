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
bool check(int X){
    if(X==1000) return false;
    int l1 = X%10;
    int l2 = (X/10) % 10;
    int l3 = (X/100);
    
    if(l3 <= l2 && l2 <= l1) return true;
    
    return false;
    
}
int main(){
    
    int T;
    
    
    freopen("/Users/thedream/Desktop/cpp/cpp/input","r",stdin);
    freopen("/Users/thedream/Desktop/cpp/cpp/output","w",stdout);
    
    scanf("%d",&T);
    
    for(int t=1;t<=T;t++){
        
        int n;
        cin >> n;
        int ans = 0;
        for(int i=n;i>=0;i--){
            if(check(i)){
                ans = i;
                break;
            }
        }
        
        printf("Case #%d: %d\n",t,ans);
    }
    
    
    return 0;
}

