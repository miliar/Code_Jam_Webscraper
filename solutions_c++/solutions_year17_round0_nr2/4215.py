#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#define ll long long
using namespace std;
int main()
{
    ll int t,a,b,i,j,k,l;
    cin>>t;
    b=1;
    k=-1;
    l=1;
    ofstream myfile;
      myfile.open ("ans1.txt");
    while(b<=t)
    {   k=-1;
        string s;
        cin>>s;
        l=1;
        for(i=0;i<s.length()-1;i++)
        {
            if(s[i]<=s[i+1])
            {
                if(s[i]<s[i+1])
                    k=i+1;
            }
            else
            {   l=-1;
                break;
            }
        }
        if(l==-1)
        {
        if(k==-1)
        {
            if(s[0]!='1')
            {
                s[0]--;
                for(i=1;i<s.length();i++)
                    s[i]='9';

            }
            else
            {
            for(i=0;i<s.length()-1;i++)
                s[i]='9';
                s.erase(s.length()-1,1);
            }
        }
        else
        {
            s[k]--;
            for(i=k+1;i<s.length();i++)
                s[i]='9';
        }
        }
    //    cout<<s<<endl;
   //     cin>>s;
        myfile<<"Case #"<<b<<": "<<s<<endl;
        b++;
    }
    myfile.close();
    return 0;
}
