#include<iostream>
#include<string>
using namespace std;
int main()
{
        int t;
        cin>>t;
        int que[t];
        string sa[t];
        for(int i=0;i<t;i++)
        {
           cin>>sa[i];
           cin>>que[i];
         }
        for(int i=1;i<=t;i++)
        {
                string s=sa[i-1];
                int k,c1=0,c2=0,flag=0;
                k = que[i-1];
                for(int j=0;j<s.length();j++)
                {    
                
                    if(s[j]=='-')
                    {
                    int count=0;
                    int j1=j;
                    while(count<k)
                    {
                        count++;
                        if(j1<s.length()&&s[j1]=='+')
                        {
                            s[j1]='-';
                            j1++;
                            c2++;
                        }
                        else if(j1<s.length()&&s[j1]=='-')
                        {
                           s[j1]='+';
                            j1++;
                        }
                        else
                        {
                        flag=1;
                        break;
                        }
                    }
                    c1++;
                    }
                }
                if(flag!=1)
                cout<<"Case #"<<i<<": "<<c1<<endl;
                else
                cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        
        }

}
