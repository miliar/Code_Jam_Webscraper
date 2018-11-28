#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("out.txt","w",stdout);
    int test,t=1;

    scanf("%d",&test);

    while(test--)
    {
        string s;
        int k;
        cin>>s>>k;
        int cnt=0;
        int l=s.size();
        for(int i=0;i<=l-k;i++)
        {
            if(s[i]=='-')
            {
                cnt++;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                    s[j]='-';

                }
            }
        }
        int ans=1;
        for(int i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                ans=0;
                break;
            }
        }
        if(ans)
        printf("Case #%d: %d\n",t++,cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n",t++,cnt);
    }
    return 0;
}
