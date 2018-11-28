#include<bits/stdc++.h>
using namespace std;
#define mx 109
char str[mx];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("small_out","w",stdout);
    int t,cs=1,n,i,j;
    scanf("%d",&t);
    while(t--){
        scanf("%s",str);
        n=strlen(str);
        for(i=1;i<n && str[i]>=str[i-1];i++);
        if(i==n){
            printf("Case #%d: %s\n",cs++,str);
            continue;
        }
        for(j=i;j<n;j++)
            str[j]='9';
        i--;
        while(i>=0){
            str[i]--;
            if(i && str[i]<str[i-1]){
                str[i]='9';
                i--;
            }
            else
                i=-1;
        }
        if(str[0]=='0')
            printf("Case #%d: %s\n",cs++,str+1);
        else
            printf("Case #%d: %s\n",cs++,str);
    }
    return 0;
}

