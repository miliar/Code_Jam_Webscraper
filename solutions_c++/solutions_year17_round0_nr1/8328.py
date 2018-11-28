#include <iostream>
using namespace std;
int main() {
    int t,k,i,c,f,m=0;
    string s;
    cin>>t;
    while(t-->0)
    {
        m++;
        cin>>s;
        cin>>k;
        
        i=0;
        c=0;
        f=0;
        while(i<s.length()-k+1)
        {
            if(s[i]=='+')
                i++;
            else
            {
                c++;
                for(int j=0;j<k;j++)
                {
                    if(s[i+j]=='+')
                        s[i+j]='-';
                    else
                        s[i+j]='+';
                }
            }
        }
        for(;i<s.length();i++)
            if(s[i]=='-')
            {
                f=1;
                break;
            }
        cout<<"\nCase #"<<m<<": ";
        if(f==0)
            cout<<c;
        else
            cout<<"IMPOSSIBLE";
        
    }
    
    return 0;

}


