#include<bits/stdc++.h>
using namespace std;
FILE *fin = freopen("in.txt","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);
int main()
{
    int t,n;
    cin>>t;
    string s;
    for(int k=1;k<=t;k++)
    {
        cin>>s>>n;
        int count=0;
        for(int i=0;i<s.length()-n+1;i++)
        {
            if(s[i]=='-')
            {
                count++;
                for(int j=i;j<i+n;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else s[j]='-';
                }
            }
        }
        int flag=1;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<endl;
                flag=0;
                break;
            }
        }
        if(flag)
        cout<<"Case #"<<k<<": "<<count<<endl;

    }
}
