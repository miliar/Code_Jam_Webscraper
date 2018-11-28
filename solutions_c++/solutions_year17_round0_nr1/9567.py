#include<stdio.h>
#include<string.h>
using namespace std;
int flips(int a[1100],int m,int n)
{
    int s[1100];
    int sum=0,ans=0;
    for(int i=0;i<m;i++)
    {
    s[i] = (a[i]+sum)%2 != 1;
    sum += s[i] - (i>=n-1?s[i-n+1]:0);
    ans += s[i];
    if(i>m-n and s[i]!=0) return -1;
    }
    return ans;
}

int main()
{
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        int k,j,m[1100],h;
        char s[1100];
        int com;
        scanf("%s",s);
         scanf("%d",&k);
         com=strlen(s);
        for(j=0;j<com;j++)
        {
            if(s[j]=='+')
              m[j]=1;
            else
              m[j]=0;
        }
        h=flips(m,com,k);
        if(h==-1)
         printf("Case #%d: IMPOSSIBLE\n",i);
        else
         printf("Case #%d: %d\n",i,h);
    }
    return 0;
}
