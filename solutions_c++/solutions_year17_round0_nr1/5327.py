#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int t=1;t<=n;t++)
    {
        string s;
        int k,flag=0,count=0;
        cin>>s>>k;
            for(int b=0;b<s.length();b++)
            {
                if(s[b]=='-')
                {
                    if(b+k>s.length())
                    {
                        flag=1;
                        break;
                    }
                    for(int c=b;c<b+k;c++)
                    s[c]=(s[c]=='+'?'-':'+');
                    count++;
                }
            }
        if(flag)
            cout<<"Case #"<<t<<": "<<"Impossible\n";
        else
            cout<<"Case #"<<t<<": "<<count<<"\n";
    }
}
