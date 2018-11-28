#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t,k,c=1;
    cin>>t;
    string s;
    while(t--)
    {
        cin>>s>>k;
        int n=s.length();
        int step=0,count=0;
        for(int i=0;i<n-k+1;i++)
        {
            if(s[i]=='-')
            {
                step++;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                    s[j]='-';
                    else
                    s[j]='+';
                    
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            if(s[i]=='+')
            count++;
        }
        if(count==n)
        cout<<"Case #"<<c++<<": "<<step<<endl;
        else
        cout<<"Case #"<<c++<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}

