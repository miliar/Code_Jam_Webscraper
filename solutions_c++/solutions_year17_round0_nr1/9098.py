#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;

    for(int tt=0;tt<t;tt++)
    {
        string s;
        int k,c=0;

        cin>>s>>k;

        //cout<<s<<" ** "<<k<<endl;

        int i;
        for(i=0;i<=s.length()-k;i++)
        {
            //cout<<"I="<<i<<" -- s="<<s<<endl;
            if(s[i] == '+')
                continue;
            c++;
            for(int kk=i;kk<k+i;kk++)
                s[kk] = s[kk]=='-'?'+':'-';
        }

        for(;i<s.length();i++)
            if(s[i]!='+')
                break;

        //cout<<"FI="<<i<<" --FS="<<s<<endl;
        if(i == s.length())
            cout<<"Case #"<<(tt+1)<<": "<<c<<endl;
        else
            cout<<"Case #"<<(tt+1)<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
