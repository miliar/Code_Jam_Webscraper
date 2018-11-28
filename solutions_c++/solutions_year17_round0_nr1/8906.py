#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char ch[1023];
int k;
void read()
{
    scanf("%s%d",ch,&k);
}
void flip(int p,int q)
{
    for(int i=p;i<=q;i++)
    {
        if(ch[i]=='-') ch[i]='+';
        else ch[i]='-';
    }
}
int solve()
{
    int n=strlen(ch),ct=0;
    for(int i=0;i+k-1<n;i++)
    {
        if(ch[i]=='-') flip(i,i+k-1),++ct;
    }
    for(int i=0;i<n;i++)
    {
        if(ch[i]=='-')
        {
            ct=-1;
            break;
        }
    }
    return ct;
}
int main()
{
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;++i)
    {
        read();
        int var=solve();
        if(var==-1) printf("Case #%d: IMPOSSIBLE\n",i);
        else printf("Case #%d: %d\n",i,var);
    }
    return 0;
}
