#include<bits/stdc++.h>
using namespace std;

const int maxn = 1e5+5;
char s[30][30];
int T,cs,m,n;

int main(){
  //  freopen("input.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.ou","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&m,&n);
        for(int i=0; i<m; ++i)scanf("%s",s[i]);
        for(int i=0; i<m; ++i)
            for(int j=0; j<n; ++j){
                if(s[i][j]!='?'){
                    for(int k=j-1; ~k && s[i][k]=='?'; --k)s[i][k]=s[i][j];
                    for(int k=j+1; k<n && s[i][k]=='?'; ++k)s[i][k]=s[i][j];
                }
            }
        for(int i=1; i<m; ++i)if(s[i][0]=='?' && s[i-1][0]!='?')
            for(int j=0; j<n; ++j)s[i][j]=s[i-1][j];
        for(int i=m-1; ~i; --i)if(s[i][0]=='?' && s[i+1][0]!='?')
            for(int j=0; j<n; ++j)s[i][j]=s[i+1][j];
        printf("Case #%d:\n",++cs);
        for(int i=0; i<m; ++i)puts(s[i]);
    }
}
