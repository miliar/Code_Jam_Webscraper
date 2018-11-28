#include<bits/stdc++.h>

using namespace std;

const int Maxn=1e3+10;

int k;
string s;
int main()
{
    int t;
    cin>>t;
    for(int o=0;o<t;o++)
    {
        cin>>s>>k;
        int n=s.length();
        int cnt=0;
        for(int i=0;i<n;i++)
            if(s[i]=='-')
            {
                for(int j=0;j<k&&i+k<=n;j++)
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else 
                        s[i+j]='-';
                cnt++;
            }

       cout<<"Case #"<<o+1<<": ";
       bool flag=0;
       for(int i=0;i<n;i++)
           if(s[i]=='-')
               flag=1;
       if(flag)
           cout<<"IMPOSSIBLE\n";
       else
           cout<<cnt<<endl;
    }
}
