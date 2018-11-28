#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,ans,i,k;
    string s;
    int p=0;
    scanf("%d",&t);
    while(t--)
    {
        ans=0;
        p++;
        cin>>s;
        int n=s.size();
        scanf("%d",&k);
        for(i=0;i+k-1<n;i++)
        {
            if(s[i]=='+')
                continue;
            else
            {
                int kk=k;
                int j=i;
                while(kk--)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                    j++;
                }
                ans++;
            }
        }
        int flag=0;
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                flag=-1;
                break;
            }
        }
        if(flag==-1)
        {
            printf("Case #%d: IMPOSSIBLE\n",p);
        }
        else
        {
            printf("Case #%d: %d\n",p,ans);
        }
    }
    return 0;
}
