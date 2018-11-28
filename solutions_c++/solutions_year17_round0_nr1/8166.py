#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string s;
        cin>>s;
        int k,c=0,i,j;
        cin>>k;
        int count=0;
        for(i=0;i<=s.length()-k;i++)
            {
            if(s[i]=='-')
                {
                count++;
                for(j=0;j<k ;j++)
                 {
                    if(s[i+j]=='-')
                    s[i+j]='+';
                    else
                        s[i+j]='-';
                }
            }
        }
        for(i=0;i<s.length();i++)
            {
            if(s[i]=='-')
                {
                c=1;
                break;
            }
        }
       // cout<<s<<" ";
        if(c==1)
            cout<< "Case #" << tt << ": IMPOSSIBLE"<<"\n";
        else
            cout<< "Case #" << tt << ": "<<count<<"\n";
        
    }
   return 0;
}