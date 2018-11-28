#include<bits/stdc++.h>
using namespace std;
#define mx 1009
char str[mx];
bool state[mx];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("small_out","w",stdout);
    int t,cs=1,n,i,j,k,cnt;
    scanf("%d",&t);
    while(t--){
        scanf("%s %d",str,&k);
        n=strlen(str);
        cnt=0;
        for(i=0;i<n;i++)
            state[i]=str[i]=='+';
        for(i=0;i<=n-k;i++){
            if(!state[i]){
                cnt++;
                for(j=0;j<k;j++)
                    state[i+j]=!state[i+j];
            }
        }
        for(;i<n;i++){
            if(!state[i])
                cnt=-1;
        }
        if(cnt<0)
            printf("Case #%d: IMPOSSIBLE\n",cs++);
        else
            printf("Case #%d: %d\n",cs++,cnt);
    }
    return 0;
}
