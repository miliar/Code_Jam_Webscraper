//marico el que lo lea
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;

#define FOR(i,f,t) for(int i=f;i<(int)t; i++)
#define FORR(i,f,t) for(int i=f;i>(int)t; i--)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define ms2(obj, val, sz) memset(obj, val, sizeof(obj[0])*sz)
#define pb push_back
#define ri(x) scanf("%d",&x)
#define rl(x) scanf("%lld",&x)
#define rii(x,y) ri(x), ri(y)

typedef vector<int> vi;
typedef long long ll;

ll N, K;
map<ll, ll> m;

int main(){
    int TC; ri(TC);
    FOR(tc,1,TC+1){
        rl(N); rl(K);
        ll y, z;
        m.clear();
        m[N]=1;
        map<ll,ll>::iterator it=m.begin();
        while(true){
            ll a = (it->first-1)/2;
            ll b = (it->first)/2;
            if(it->second >= K){
                y=b;
                z=a;
                break;
            }
            K-=it->second;
            m[a] += it->second;
            m[b] += it->second;
            it--;
        }
        printf("Case #%d: %lld %lld\n",tc,y,z);
    }
}
