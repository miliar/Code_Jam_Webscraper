#include<bits/stdc++.h>
using namespace std;

char s[30];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long t,ti,l,i,j,k,ans;
    scanf("%lld",&t);
    for(ti=1; ti<=t; ++ti)
    {
        scanf("%s",s);
        l=strlen(s);
        for(i=0; i<l-1; ++i)
        {
            if(s[i]>s[i+1])
            {
                for(j=i; j>=0; --j)
                {
                    if(s[j]<s[i])
                        break;
                }
                ++j;
                s[j]--;
                for(++j; j<l; ++j)
                    s[j]='9';
                break;
            }
        }
        ans=0;
        for(i=0; i<l; ++i)
            ans=(ans*10)+s[i]-'0';
        printf("Case #%lld: %lld\n",ti,ans);
    }
    return 0;
}
