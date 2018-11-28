#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,k,i,flag,l,flip,j;
    string s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s>>k;
        l=s.length();
        flag=1;
        flip=0;
        for(j=0;j<l;j++)
        {
            if(s[j]=='-')
            {
                s[j]='+';
                flip++;
                if(j+k>l)
                {
                    flag=0;
                    break;
                }
                else
                {
                    for(int q=j;q-j<k;q++)
                    {
                        if(s[q]=='+')
                            s[q]='-';
                        else
                            s[q]='+';
                    }
                        
                }
                    
            }
        
        }
        if(flag)
            cout<<"Case #"<<i<<": "<<flip<<endl;
            else
                cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
    
}
