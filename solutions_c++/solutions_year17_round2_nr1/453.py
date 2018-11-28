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

bool isPrime(int X){
    if(X==1) return true;
    for(int i=2;i*i<=X;i++){
        if(X%i==0) return false;
    }
    return true;
}

int main(){
    
    int T;
    
    
    freopen("/Users/thedream/Desktop/cpp/cpp/input","r",stdin);
    freopen("/Users/thedream/Desktop/cpp/cpp/output","w",stdout);
    
    scanf("%d",&T);
    
    for(int t=1;t<=T;t++){
        
        int D, N;
        cin >> D >> N;
        double ans = numeric_limits<double>::max();
        double x, y;
        for(int i=0;i<N;i++){
            cin >> x >> y;
            
            ans = min(ans, (D * y)/(D-x));
        }
        
        printf("Case #%d: %.6lf\n",t,ans);
        
    }
    
    
    return 0;
}

