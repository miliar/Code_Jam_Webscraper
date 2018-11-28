#include<bits/stdc++.h>
using namespace std;

int f[1111];
int T;
string str;
int len;
int k;

int ans1,ans2;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    for(int it=1;it<=T;it++)
    {
        cin>>str>>k;
        len=str.length();
        ans1=ans2=0;

        for(int i=1;i<=len;i++)
            f[i]=str[i-1]=='+'?1:0;
        for(int i=1;i<=len-k+1;i++)
            if(f[i]==0)
            {
                ans1++;
                for(int j=0;j<k;j++)
                    f[i+j]=1-f[i+j];
            }
        for(int i=1;i<=len;i++)
            if(f[i]!=1)
                ans1=0x3f3f3f3f;

        for(int i=1;i<=len;i++)
            f[i]=str[i-1]=='+'?1:0;
        for(int i=len;i>=k;i--)
            if(f[i]==0)
            {
                ans2++;
                for(int j=0;j<k;j++)
                    f[i-j]=1-f[i-j];
            }
        for(int i=1;i<=len;i++)
            if(f[i]!=1)
                ans2=0x3f3f3f3f;
        
        ans1=min(ans1,ans2);
        if(ans1!=0x3f3f3f3f)
            printf("Case #%d: %d\n",it,ans1);
        else
            printf("Case #%d: IMPOSSIBLE\n",it);
    }

    return 0;
}

