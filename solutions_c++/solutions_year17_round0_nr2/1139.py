#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string s;
        int i,n,k,flag=0,ans=0;
        cin>>s;
        n=s.size();
        ans=n;
        for(i=n-2;i>=0;i--)
        {
            if(s[i]>s[i+1])
            {
                s[i]--;
                ans=i+1;
            }
        }
        cout<<"Case #"<<tt<<": ";
        i=0;
        if(s[0]=='0')
            i++;
        for(;i<ans;i++)
            cout<<s[i];
        for(i=ans;i<n;i++)
            cout<<"9";
        cout<<"\n";
    }
    return 0;
}
