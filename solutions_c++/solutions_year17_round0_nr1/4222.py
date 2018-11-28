#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        cin>>s;
        int k;
        cin>>k;
        int ans = 0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                if(i+k-1>=s.size())
                {
                    ans = -1;
                    break;
                }
                ans++;
                for(int flip=0;flip<k;flip++)
                {
                    if(s[flip+i]=='-')
                        s[flip+i]='+';
                    else
                        s[flip+i]='-';
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        if(ans==-1)
            cout<<"IMPOSSIBLE";
        else
            cout<<ans;
        cout<<endl;
    }
    return 0;
}
