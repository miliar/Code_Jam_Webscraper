#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,t;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(t = 1; t<=T; t++)
    {
        string s;
        int k;
        cin>>s>>k;
        int cut=0;
        for(int i=0;i<=s.length()-k;i++)
        {
            if(s[i] == '-')
            {
                int guno=0;
               for(int j=i;j<i+k;j++)
               {
                  if(s[j]=='-') s[j] = '+';
                  else s[j] = '-';
                  guno++;
               }
               if(guno==k)cut++;

            }
        }
        bool ok=true;
        for(int i=0;i<s.length();i++)
        {
            if(s[i] == '-')
            {
                ok = false;
                break;
            }
        }
        if(ok)
        {
            printf("Case #%d: %d\n",t,cut);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n",t);
        }
    }
    return 0;
}
