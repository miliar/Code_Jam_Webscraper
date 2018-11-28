#include<stdio.h>
#include<math.h>
#include<string.h>
#include<iostream>
using namespace std;
int res[1010];
int judge(int x)
{
    int now=10;
    while(x)
    {
        if(x%10>now)
            return 0;
        now=x%10;
        x/=10;
    }
    return 1;
}
int main()
{
    int t;
   // cout<<judge(129)<<endl;
   freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    memset(res,0,sizeof(res));
    for(int i=1;i<=1000;i++)
    {
        if(judge(i))res[i]=i;
        else res[i]=res[i-1];
    }
    int ca=1;
    while(t--)
    {
        int x;
        cin>>x;
        printf("Case #%d: ",ca++);
        cout<<res[x]<<'\n';
    }
    return 0;
}
