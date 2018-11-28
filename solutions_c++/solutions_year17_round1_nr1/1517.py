
#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <set>
#include <stdio.h>
#include <string>
#include <time.h>
#include <vector>
using namespace std;
#define LL long long
#define pi acos(-1.0)
#pragma comment(linker, "/STACK:1024000000")
const int mod=1e9+7;
const int INF=0x3f3f3f3f;
const double eqs=1e-9;
const int MAXN=200000+10;
char s[30][30];
int main()
{
    int t, icase=0, n, m, i, j;
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++){
            scanf("%s",s[i]);
        }
        for(i=0;i<n;i++){
            for(j=1;j<m;j++){
                if(s[i][j]=='?'&&s[i][j-1]!='?'){
                    s[i][j]=s[i][j-1];
                }
            }
        }
        for(i=0;i<n;i++){
            for(j=m-2;j>=0;j--){
                if(s[i][j]=='?'&&s[i][j+1]!='?'){
                    s[i][j]=s[i][j+1];
                }
            }
        }
        for(i=1;i<n;i++){
            for(j=0;j<m;j++){
                if(s[i][j]=='?'&&s[i-1][j]!='?'){
                    s[i][j]=s[i-1][j];
                }
            }
        }
        for(i=n-2;i>=0;i--){
            for(j=0;j<m;j++){
                if(s[i][j]=='?'&&s[i+1][j]!='?'){
                    s[i][j]=s[i+1][j];
                }
            }
        }
        printf("Case #%d:\n",++icase);
        for(i=0;i<n;i++){
            printf("%s\n",s[i]);
        }
    }
    return 0;
}
