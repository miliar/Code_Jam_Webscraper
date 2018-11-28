#include <bits/stdc++.h>
#define ll long long
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ll int a,b,c,d,l,i,j,k,t;
    cin>>t;
    ofstream myfile;
    b=1;
    myfile.open ("example.txt");
    while(b<=t)
    {
    string s;
    j=0;
    d=0;
    cin>>s;
    
    //  myfile.open ("ans.txt");
//    k=s.length();
//    cout<<k;
//    cout<<s;
    cin>>k;
  //  cin>>d;
        for(i=0;i<s.length()-k+1;i++)
        {
             if(s[i]=='-')
             {
                for(c=i;c<i+k;c++)
                {
                    if(s[c]=='-')
                        s[c]='+';
                    else
                        s[c]='-';
                }
                j++;
             }
        }
     //   cin>>c;
        for(c=i-1;c<s.length();c++)
        {
            if(s[c]=='+')
            {
                d++;
            }
        }
     //   cout<<s;
        if(d==k)
        myfile<<"Case #"<<b<<": "<<j<<endl;
        else
        myfile<<"Case #"<<b<<": IMPOSSIBLE"<<endl;
        b++;
    }
     myfile.close();
    return 0;
}
