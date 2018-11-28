#include<bits/stdc++.h>
using namespace std;


int main()
{
    int t,k,i,j,r;
    string s;
    cin>>t;
    for(int ti=1;ti<=t;ti++)
    {
        cin>>s>>k;
        r=0;
        for(i=0;i<s.length();i++)
            if((s[i]=='-')&&(i+k<=s.length()))
            {
                for(j=i;j<k+i;j++)
                    s[j]=s[j]=='-'?'+':'-';
                r++;
                //cout<<s<<endl;
            }
        for(i=0;i<s.length();i++)
            if(s[i]=='-')   break;
        if(i==s.length())   cout<<"Case #"<<ti<<": "<<r<<endl;
        else    cout<<"Case #"<<ti<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}