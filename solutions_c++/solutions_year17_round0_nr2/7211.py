#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int cases=1;cases<=t;cases++)
    {
        string s;
        cin>>s;
        if(s.size()<2)
        {
            cout<<"Case #"<<cases<<": "<<s[0]<<endl;
            continue;
        }
        // cout<<s<<endl;
        int i;
        int j=-1;
        for(i=s.size()-1;i>0;i--)
        {
            if(s[i]<s[i-1])
            {
                s[i]='9';
                s[i-1]--;
                j=i;
            }
            else if(s[i]==s[i-1]&&s[i]=='0')
            {
                 s[i]='9';
                s[i-1]--;
            }        
        }
        if(j!=-1)
        {
            for(;j<s.size();j++)
            s[j]='9';
        }
        cout<<"Case #"<<cases<<": ";
        if(s[0]>'0')
        cout<<s[0];
        for(int i=1;i<s.size();i++)
        if(s[i]>='0')
        cout<<s[i];
        cout<<endl;
    }

    return 0;
}