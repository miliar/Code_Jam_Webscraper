#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.out","w",stdout);
    int T,i,j,k,v;
    string str;
    cin>>T;
    v=T;
    while(T--)
    {
        cin>>str>>k;
        int l=str.length(),ans=0,c=0;
        for(i=0;i<=l-k;i++)
        {
            if(str[i]=='+')
                continue;
            for(j=i;j<i+k;j++)
            {
                if(str[j]=='+')
                    str[j]='-';
                else
                    str[j]='+';
            }
            ans++;
        }
        for(i=0;i<l;i++)
        {
            if(str[i]=='-')
            {
                c=1;
                break;
            }
        }
        cout<<"Case #"<<v-T<<": ";
        if(c==1)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<endl;
    }
}
