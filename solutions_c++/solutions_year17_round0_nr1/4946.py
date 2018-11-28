#include <bits/stdc++.h>

#define MAX 100000
#define INF 2000000000

typedef long long ll;
typedef unsigned long long llu;

using namespace std;

void IO()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
}

int main()
{
    //IO();
    int t,k;
    char str[10005];
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++){
        scanf("%s %d",str,&k);
        int cnt=0;
        int len=strlen(str);
        for(int i=0;((i+k)-1)<len;i++){
            if(str[i]=='-'){
                cnt++;
                for(int j=i;j<(i+k);j++){
                    str[j]=='-'?str[j]='+':str[j]='-';
                }
            }
        }
        bool flag=true;
        for(int i=0;i<len&&flag;i++){
            if(str[i]=='-')flag=false;
        }
        printf("Case #%d: ",tc);
        if(flag)printf("%d\n",cnt);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
