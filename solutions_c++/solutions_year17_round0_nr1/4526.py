#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("D:\A-large.in","r",stdin);
    freopen("D:\A-large.out","w",stdout);
    string s;
    int t,l,case1=0;
    scanf("%d",&t);
    while(case1++<t)
    {
        bool ok=true;
        int p=0,m=0,k;
        cin>>s>>k;
        l=s.length();
        int ans=0;
        bool found=false;
        for(int i=0;s[i]&&ok;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=0;j<k;j++)
                {
                    if(j>=l||i+k>l)
                    {
                        ok=false;
                        break;
                    }
                    else
                    {
                        if(s[j+i]=='-') s[j+i]='+';
                        else s[j+i]='-';
                    }
                }
                i=0;
            }
        }
        printf("Case #%d: ",case1);
        if(ok) cout<<ans<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
