#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,t=0,k,lim,out;
    bool bol=1;
    string s;
    cin>>T;
    while(T--)
    {
        bol=1;
        out=0;
        cin>>s>>k;
        lim=s.length();
        for(int i=0;i<lim&&bol;i++)
        {

            if(s[i]=='-')
            {
                out++;
                if(i+k>lim)bol=0;
                else
                {
                    for(int j=i;j<i+k;j++)
                    {
                        if(s[j]=='-')s[j]='+';
                        else s[j]='-';
                    }
                }
            }
        }
        printf("Case #%d: ",++t);
        if(bol)printf("%d\n",out);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
