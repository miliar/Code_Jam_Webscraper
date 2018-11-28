#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define FOR(i, j, k) for(int i = j;i<= k;i++)
#define ll long long
const int maxn  =50;
void fastmod(int a, int b)
{
    while(b)
    {
        b >>= 1;
        a *= a ;
        a %= 100;
    }
}
char s[30][30];
int main(){
    freopen("/Users/hermione/Desktop/in.txt","r",stdin);
    freopen("/Users/hermione/Desktop/temp.txt", "w", stdout);
    int t;
    cin>>t;
    
    FOR(z, 1, t){
        int r,c;
        fastmod(1,1);
        fastmod(2,1);
        cin>>r>>c;
        FOR(i, 0, r-1)
            cin>>s[i];
        FOR(i, 0, r-1){
            FOR(j, 0, c-1){
                if(s[i][j]!='?'){
                    for(int k=j+1;k<c;k++){
                        if(s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                    }
                    for(int k=j-1;k>=0;k--){
                        if(s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                    }
                }
            }
        }
        FOR(i, 0, r-1){
            if(s[i][0]!='?'){
                for(int k=i-1;k>=0;k--){
                    if(s[k][0]=='?'){
                        for(int j=0;j<c;j++) s[k][j]=s[i][j];
                    }
                    else break;
                }
                for(int k=i+1;k<r;k++){
                    if(s[k][0]=='?'){
                        for(int j=0;j<c;j++) s[k][j]=s[i][j];
                    }
                    else break;
                }
            }
        }
        
        printf("Case #%d:\n",z);
        FOR(i, 0, r-1) printf("%s\n",s[i]);
        
    }
    return 0;
}