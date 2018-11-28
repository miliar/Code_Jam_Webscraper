#include<iostream>
#include<string>
#include<Stdlib.h>
using namespace std;
int main()
{

    int t;
    cin>>t;
    int g=1;
    while(g<=t)
    {
        string s,n;
        cin>>s;
        n="";
        n+=s[0];
        int i,pos=1;
        for( i=1;i<s.length();i++)
        {
            if(s[i-1]<=s[i])
            {
                 n+=s[i];

            }
            else
            {

                 break;
            }

        }
        pos=i;
        for(;i<s.length()&&pos<s.length();i++)
            n+='9';

       // cout<<n<<" "<<pos<<endl;
        if(pos<s.length())
            n[pos-1]-=1;

        for(i=pos-1;i>0&&pos<s.length();i--)
        {
            if(n[i-1]>n[i])
            {
                n[i-1]-=1;
                n[i]='9';
            }


        }

       if(n[0]=='0')
        n.erase(n.begin());

       cout<<"Case #"<<g<<": "<<n<<endl;
       g++;
    }

}
