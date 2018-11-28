#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int kk=0;kk<t;kk++)
    {
        string s;
        int k;
        cin>>s;
        cin>>k;
        int l=s.length(),f=0;
        long long co=0;
        for(int i=0;i<l&&f==0;i++)
        {
            if(s[i]=='-')
            {
                if(i+k-1<l)
                {
                    for(int j=i;j<=i+k-1;j++)
                    {
                        if(s[j]=='+')
                        s[j]='-';
                        else
                        s[j]='+';
                    }
                    co++;
                }
                else
                f=1;
            }
        }
        if(f==0)
        {
            cout<<"Case #"<<kk+1<<": "<<co<<endl;
        }
        else
        {
            cout<<"Case #"<<kk+1<<": "<<"IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
