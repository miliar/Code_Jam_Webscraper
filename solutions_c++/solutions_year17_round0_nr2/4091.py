#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        string s;
        cin>>s;
        int bre=s.length();
        for(int i=0;i<s.length()-1;i++)
        {
            if(s[i]>s[i+1])
            {
                bre=i;
                s[i]--;
                break;
            }
        }
       // cout<<bre<<"@";
        cout<<"Case #"<<k<<": ";
        if(bre==s.length())
        {
            cout<<s<<"\n";
            continue;
        }
        for(int i=bre+1;i<s.length();i++)
        {
            s[i]='9';
            //cout<<"#";
        }

        for(int i=bre;i>0;i--)
        {
            if(s[i]<s[i-1])
            {
                s[i]='9';
                s[i-1]--;
            }
            else
              break;
        }

        for(int i=0;i<s.length();i++)
        {
            if(i==0 && s[i]=='0')
               continue;
            cout<<s[i];
        }
        cout<<"\n";
    }
return 0;
}


