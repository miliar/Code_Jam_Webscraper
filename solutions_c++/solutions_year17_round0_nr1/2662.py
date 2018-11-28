#include <iostream>
#include<cstring>
#include<stdio.h>
using namespace std;
#define nmax 1005
int t, k, n, sum,rez, v[nmax], val;
char s[nmax];
bool ok;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++){
        scanf("%s %d",&s,&k);
        n=strlen(s);
        rez=sum=0;
        for (int i=0;i<n-k+1;i++){
            sum+=v[i];  sum&=1;
            val=(s[i]=='+');
            if ((sum^val)==0){
                sum^=1;
                v[i+k]++;  v[i+k]&=1;
                rez++;
            }
        }
        ok=1;
        for (int i=n-k+1;i<n;i++){
            sum+=v[i];  sum&=1;
            if (((sum==1)&&(s[i]=='+'))|| ((sum==0)&&(s[i]=='-'))){
                ok=0;   
                break;
            }
        }
        if (ok)
            printf("Case #%d: %d\n",ii,rez);
        else
            printf("Case #%d: IMPOSSIBLE\n",ii);
        for (int i=0;i<=n;i++)
            v[i]=0;
    }
    return 0;
}
