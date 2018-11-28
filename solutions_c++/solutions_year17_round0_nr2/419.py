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

ll p[20], N;
int A;

ll ans;
bool f(int a, int dd){
    if(a==-1){
        ans=0;
        return true;
    }
    int d = (N/p[a])%10;
    if(dd>d) return false;
    if(f(a-1, d)){
        ans += d*p[a];
        return true;
    }else if(d>dd){
        ans = d*p[a]-1;
        return true;
    }
    return false;
}

int main(){
    p[0]=1;
    FOR(i,1,19) p[i]=10*p[i-1];
    int TC; ri(TC);
    FOR(tc,1,TC+1){
        rl(N);
        FOR(i,0,19) if(N/p[i]) A=i;
        f(A,0);
        printf("Case #%d: %lld\n",tc,ans);
    }
}
