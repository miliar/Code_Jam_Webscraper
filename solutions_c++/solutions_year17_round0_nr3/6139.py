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

int main(){
    
    int T;
    
    
    freopen("/Users/thedream/Desktop/cpp/cpp/input","r",stdin);
    freopen("/Users/thedream/Desktop/cpp/cpp/output","w",stdout);
    
    scanf("%d",&T);
    
    for(int t=1;t<=T;t++){
        
        int y,z;
        priority_queue<pair<int,pair<int,int> > > que;
        
        vector<int> v;
        int N,K;
        cin >> N >> K;
        que.push(make_pair(N-1,make_pair(N-1,N)));
        for(int i=1;i<=K;i++){

            int s = N - que.top().second.first;
            int e = que.top().second.second;
            que.pop();
            int m = (s+e) / 2;
            v.push_back(m);
            
            if(m-s>0) que.push(make_pair(m-s,make_pair(N-s,m-1)));
            if(e-m>0) que.push(make_pair(e-m,make_pair(N-(m+1),e)));
        }
        int last = v[v.size()-1];
        v.push_back(0);
        v.push_back(N+1);
        sort(v.begin(),v.end());
        int l,r;
        for(int i=1;i<v.size();i++){
            if(v[i] == last) {
                l = v[i-1];
                r = v[i+1];
                break;
            }
        }
        y = max(last-l, r-last);
        z = min(last-l, r-last);
        printf("Case #%d: %d %d\n",t,y-1,z-1);
    }
    
    
    return 0;
}

