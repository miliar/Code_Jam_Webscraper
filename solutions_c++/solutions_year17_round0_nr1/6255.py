#include <iostream>
#include<string>
using namespace std;

int main() {
    long t;
    cin>>t;
    for(long r=1;r<=t;r++)
    {
        string s;
        cin>>s;
        long k,l,i,j,count=0;
        cin>>k;
        l=s.size();
        for(i=0;i<=l-k;i++)
        {
            if(s[i]=='-')
            {    count++;
                for(j=i;j<i+k;j++)    
                {
                    if(s[j]=='-')    s[j]='+';
                    else s[j]='-';
                }
            }
        }
        int flag=0;
        
        for(j=i;j<l;j++)
        {
            if(s[j]=='-')    
            {
                flag=1;
                break;
            }
        }
        if(flag==1)        cout<<"Case #"<<r<<": "<<"IMPOSSIBLE"<<endl;
        else        cout<<"Case #"<<r<<": "<<count<<endl;
    }
    return 0;
}