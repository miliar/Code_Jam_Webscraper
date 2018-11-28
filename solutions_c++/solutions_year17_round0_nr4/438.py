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

const int MAXN = 102;

int N, M;
char grid[MAXN];

int main(){
    int TC; ri(TC);
    FOR(tc,1,TC+1){
        rii(N,M);
        ms(grid,'.');
        int ox = -1;
        FOR(i,0,M){
            char ch[2]; scanf("%s",ch); int r, c; rii(r,c); r--; c--;
            grid[c] = ch[0];
            if(ch[0]=='o' || ch[0] == 'x'){
                ox = c;
            }
        }
        vector<pair<char, pair<int, int> > > change;
        if(ox==-1){
            ox=0;
            change.pb({'o',{0+1,0+1}});
            grid[ox]='o';
        }else if(grid[ox]=='x'){
            change.pb({'o',{0+1,ox+1}});
            grid[ox]='o';
        }
        if(N==1){
            printf("Case #%d: 2 %d\n",tc,(int)change.size());
            FOR(i,0,change.size()) printf("%c %d %d\n",change[i].first,
                change[i].second.first,change[i].second.second);
            continue;
        }
        FOR(c,0,N) if(grid[c]=='.') change.pb({'+',{0+1,c+1}});
        FOR(c,1,N-1) change.pb({'+',{N,c+1}});
        FOR(c,1,N){
            if(ox==c) change.pb({'x',{c+1,1}});
            else change.pb({'x',{c+1,c+1}});
        }
        printf("Case #%d: %d %d\n",tc,3*N-2,(int)change.size());
            FOR(i,0,change.size()) printf("%c %d %d\n",change[i].first,
                change[i].second.first,change[i].second.second);
    }
}
