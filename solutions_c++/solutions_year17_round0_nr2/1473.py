
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
char s[20];
int main()
{
    int len, i, j, t, icase=0, pos, start;
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%s",s);
        icase++;
        printf("Case #%d: ",icase);
        len=strlen(s);
        pos=len;
        for(i=1;i<len;i++){
            if(s[i]<s[i-1]){
                pos=i;
                break;
            }
        }
        if(pos!=len){
            for(i=pos-2;i>=0;i--){
                if(s[i]!=s[i+1])
                    break;
            }
            s[i+1]-=1;
            for(j=i+2;j<len;j++)
                s[j]='9';
        }
        if(s[0]=='0') start=1;
        else start=0;
        for(i=start;i<len;i++){
            printf("%c",s[i]);
        }
        puts("");
    }
    return 0;
}
