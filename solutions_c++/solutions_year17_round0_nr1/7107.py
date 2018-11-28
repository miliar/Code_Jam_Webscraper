#include<bits/stdc++.h>
using namespace std;

int t,k,ans=0,cas=0;
string str;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    while(t--)
    {
        cas++;
        ans=0;
        cin>>str>>k;

        for(i=0; i<str.length()-k+1; i++)
        {
            if(str[i]=='+')
                continue;
            for(j=0; j<k; j++)
            {
                if(str[i+j]=='+')
                    str[i+j]='-';
                else
                    str[i+j]='+';
            }
            ans++;
        }

        for(i=0;i<str.length();i++)
            if(str[i]=='-')
                break;

        if(i==str.length())
            printf("Case #%d: %d\n",cas,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",cas);
    }
    return 0;
}
