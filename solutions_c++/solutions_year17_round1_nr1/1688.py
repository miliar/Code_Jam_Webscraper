#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <deque>

using namespace std;
typedef long long LL;

char g[32][32];
bool vis[32][32];
int r,c;

bool checkEmpty(int x, int l, int r) {
    for(int i = l; i<= r; i++){
        if(g[x][i]!='?')
            return false;
    }
    return true;
}

void extend(int x, int y){
    vis[x][y] = true;
    char curr = g[x][y];
    int left = y;
    int right = y;
    for(int i = y-1; i >0; i--) {
        if(g[x][i]!='?')
            break;
        left = i ;
        g[x][i] = curr;  
        vis[x][i] =true;
    }
    for(int i=y+1;i<=c;i++) {
        if(g[x][i]!='?')
            break;
        right = i;
        g[x][i] = curr;    
        vis[x][i] = true;
    }
    //
    for(int i = x-1; i>0; i--) {
        if(!checkEmpty(i,left,right))
            break;
        for(int j = left; j<=right; j++){
            g[i][j] = curr;
            vis[i][j] = true;
        }
    }
    for(int i = x+1; i<=r; i++) {
        if(!checkEmpty(i,left,right))
            break;
        for(int j = left; j<=right; j++){
            g[i][j] = curr;
            vis[i][j] = true;
        }
    }
    return ;
}
int main() {
     ios::sync_with_stdio(false);
     int T;
     cin >> T;
     for (int pp = 1; pp <= T; pp++) {
         printf("Case #%d:\n", pp);
         cin>>r>>c;
         for (int i = 1; i <= r; i++) {
             scanf("%s",g[i]+1);
         }
         memset(vis,0,sizeof(vis));
         for (int i = 1; i <= r; i++) {
             for (int j = 1; j<= c; j++) {
                 if(g[i][j] != '?' && !vis[i][j]) {
                     extend(i,j);
                 }
             }
         }
         for (int i = 1; i <= r; i++) {
             for(int j=1;j<=c;j++)
                cout<<g[i][j];
             cout<<endl;
         }
     } 
     return 0;
}