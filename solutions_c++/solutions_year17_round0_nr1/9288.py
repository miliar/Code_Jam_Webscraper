#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k,i,j,cnt;
    cin>>t;
    int x=1;
    while(x<=t)
    {
        string s;
        int flag=0;
        cnt=0;
        cin>>s;
        cin>>k;
        int len=s.size();
        for(i=0;i<len;i++)
        {
            if(s[i]=='-'&&i+k-1<len)
            {
                cnt++;
                for(j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                    s[j]='+';
                    else
                     s[j]='-';
                }
            }
        }
       // cout<<s<<endl;
        for(i=0;i<len;i++)
        {
            if(s[i]=='-')
            {
                flag=1;
                break;
            }
        }
        cout<<"Case #"<<x<<": ";
        if(flag==0)
        {
            cout<<cnt;
        }
        else
        {
            cout<<"IMPOSSIBLE";
        }
        cout<<endl;

      x++;
    }
    return 0;
}
