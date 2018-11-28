#include <iostream>
using namespace std;

int main()
{
    int t=0;
    cin>>t;
    
    string s;
    int k=0;
    for(int u=1;u<=t;u++)
    {
        cin>>s;
        cin>>k;
        
        int ways=0;
        int check=0;
        for(int i=0;i<=s.length()-1;i++)
        {
            if(s[i]=='-')
            {
                if(i+k-1>=s.length())
                {
                    //cout<<"IMPOSSIBLE\n";
                    check=1;
                    break;
                }
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
                ways+=1;
            }
            //cout<<s<<"\n";
        }
        if(check==0)
        {
            int nope=0;
            for(int i=0;i<s.length();i++)
            {
                if(s[i]=='-')
                {
                    nope=1;
                    break;
                }
            }
            if(nope==0)
                cout<<"Case #"<<u<<": "<<ways<<"\n";
            else
                cout<<"Case #"<<u<<": "<<"IMPOSSIBLE\n";
        }    
        else
            cout<<"Case #"<<u<<": "<<"IMPOSSIBLE\n";
    }
    return 0;
}
