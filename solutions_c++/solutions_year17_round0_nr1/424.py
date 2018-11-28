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
#define rii(x,y) ri(x), ri(y)

typedef vector<int> vi;
typedef long long ll;

const int MAXN = 1e3+3;

int N, K;
char S[MAXN];

int main(){
    int TC; ri(TC);
    FOR(tc,1,TC+1){
        scanf("%s",S); ri(K);
        N = strlen(S);
        int ans = 0;
        FOR(i,0,N-K+1){
            if(S[i]=='-'){
                ans++;
                FOR(j,i,i+K) S[j] = (S[j]=='+' ? '-' : '+');
            }
        }
        bool good = true;
        FOR(i,0,N) if(S[i]=='-') good=false;
        printf("Case #%d: ",tc);
        if(good) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
}
