#include <bits/stdc++.h>

using namespace std;

#define si(a) scanf("%d",&a)
#define MAX 1005

char str[MAX];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t;
    si(t);
    for(int ca=1;ca<=t;ca++){
        int n,i,d,cnt=0;
        scanf("%s",str);
        si(d);
        n=strlen(str);
        printf("Case #%d: ",ca);
        for(i=0;i<n;i++){
            if(str[i]=='+')continue;
            if(n-i<d){
                printf("IMPOSSIBLE\n");
                break;
            }
            cnt++;
            for(int j=0;j<d;j++){
                if(str[i+j]=='-')str[i+j]='+';
                else str[i+j]='-';
            }
        }
        if(i==n)printf("%d\n",cnt);
    }
    return 0;
}
