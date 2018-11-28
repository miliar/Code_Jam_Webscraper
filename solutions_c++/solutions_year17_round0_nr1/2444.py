#include<bits/stdc++.h>
using namespace std;

#define MAX 1010

char s[MAX];

void flip(int l,int r)
{
    int i;
    for(i=l; i<=r; ++i)
    {
        if(s[i]=='-')
            s[i]='+';
        else
            s[i]='-';
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ti,l,i,j,k,ans;
    scanf("%d",&t);
    for(ti=1; ti<=t; ++ti)
    {
        ans=0;
        scanf("%s %d",s,&k);
        l=strlen(s);
        for(i=0; i<l; ++i)
        {
            if(i+k-1>=l)
                break;
            if(s[i]=='-')
            {
                flip(i,i+k-1);
                ++ans;
            }
        }

        for(i=0; i<l; ++i)
        {
            if(s[i]=='-')
                ans=-1;
        }
        if(ans==-1)
            printf("Case #%d: IMPOSSIBLE\n",ti);
        else
            printf("Case #%d: %d\n",ti,ans);
    }
    return 0;
}
