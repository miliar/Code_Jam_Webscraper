#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;cin>>test;
    for(int t=1;t<=test;t++)
    {
        string s;cin>>s;int x;cin>>x;
        int k=0;int len=s.size();
        for(int i=0;i<=len-x;i++)
        {
            if(s[i]=='-')
            {
                ++k;
                for(int j=i;j<i+x;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
            }
            //cout<<s<<endl;

        }
        cout<<"Case #"<<t<<":"<<" ";
        int flag=1;
        for(int p=len-x;p<len;p++)
        {
            if(s[p]=='-')
                flag=0;
        }
        if(flag==0)
            cout<<"IMPOSSIBLE"<<endl;
        if(flag==1)
            cout<<k<<endl;
    }
}
