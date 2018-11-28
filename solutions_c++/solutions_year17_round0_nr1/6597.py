#include <iostream>
#include <string>
using namespace std;

int main()
{
    freopen ("/Users/utkarsh/Xcode_C++/Random/Random/K1/K1/inp.txt","r",stdin);
    freopen ("/Users/utkarsh/Xcode_C++/Random/Random/K1/K1/o.txt","w",stdout);
    int t;
    cin>>t;
    for(int a=1;a<=t;a++)
    {
    string s;
    int k;
    cin>>s;
    cin>>k;
    int count=0;
    for(int i=0;i<s.length()-k+1;i++)
    {
        if(s[i]=='-')
        {
            for(int j=0;j<k;j++)
            {
                if(s[i+j]=='+')
                    s[i+j]='-';
                else
                    s[i+j]='+';
            }
            count++;
        
        }
    }
    bool flag=false;
    for(int i=s.length()-k+1;i<s.length();i++)
    {
        if(s[i]=='-')
            flag=true;
            
    }
    if(flag)
        cout<<"Case #"<<a<<": IMPOSSIBLE"<<endl;
    else
        cout<<"Case #"<<a<<": "<<count<<endl;
    }
}
