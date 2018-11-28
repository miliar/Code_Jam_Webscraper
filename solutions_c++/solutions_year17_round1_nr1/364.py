//marico el que lo lea
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
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

char grid[27][27];
int R, C;

int main(){
    int TC; ri(TC);
    FOR(tc,1,TC+1){
        rii(R,C);
        FOR(r,0,R) scanf("%s",grid[r]);
        FOR(r,0,R){
            char last = '?';
            FOR(c,0,C){
                if(grid[r][c] != '?') last = grid[r][c];
                grid[r][c] = last;
            }
            last = '?';
            FORR(c,C-1,-1){
                if(grid[r][c] != '?') last = grid[r][c];
                grid[r][c] = last;
            }
        }
        FOR(r,0,R-1){
            if(grid[r+1][0] == '?') FOR(c,0,C) grid[r+1][c] = grid[r][c];
        }
        FORR(r,R-1,0){
            if(grid[r-1][0] == '?') FOR(c,0,C) grid[r-1][c] = grid[r][c];
        }
        printf("Case #%d:\n",tc);
        FOR(r,0,R){
            FOR(c,0,C) printf("%c",grid[r][c]);
            printf("\n");
        }
    }
}
