#include <iostream>
using namespace std;

int main()
{
    string s;
    int t,n,f=0,k,l=0,flag=0,i,j;
    cin>>t;
    while(t--)
    {   f=0;
       flag=0;
       l++;
        cin>>s;
        cin>>k;
        n=s.length();
        for(i=0;i<=n-k;i++)
        {  
            if(s[i]=='-')
            {   f++;
               s[i]='+';
            for(j=1;j<k;j++)
            {
                if(s[i+j]=='+')
                s[i+j]='-';
                else
                s[i+j]='+';
            }
            }
        }
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
                flag=1;
            
        }
        if(flag==0)
        cout<<"Case #"<<l<<": "<<f<<endl;
        else
        cout<<"Case #"<<l<<": "<<"IMPOSSIBLE"<<endl;
    }
    //cout << "Hello World!" << endl;
    return 0;
}
