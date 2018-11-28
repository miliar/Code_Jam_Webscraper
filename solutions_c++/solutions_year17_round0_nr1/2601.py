#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,j,m;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        char S[1005];
        int K,ans=0;
        scanf("%s",S);
        int l=strlen(S);
        cin>>K;
        for(j=0;j+K<=l;j++)
        {
            if(S[j]=='-')
            {
                for(m=0;m<K;m++)
                {
                    if(S[j+m]=='-')
                        S[j+m]='+';
                    else
                        S[j+m]='-';
                }
                ans++;
            }
        }
        for(j=0;j<l;j++)
            if(S[j]=='-')
                ans=-1;
        cout<<"Case #"<<i<<": ";
        if(ans==-1)
            cout<<"IMPOSSIBLE";
        else
            cout<<ans;
        cout<<endl;
    }
}
