#include<bits/stdc++.h>
#define ll long long

using namespace std;
typedef pair<int,int> pii;
//long long int;

int main()
{
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        long long int n;
        cin>>n;
        string s="";
        long long int t;
        t=n;
        while(t!=0)
        {
            int d=t%10;
            char c=d+48;
            s=c+s;
            t/=10;
        }
        int flag=0;
        for(int j=1;j<=19;j++){
        flag=0;
        for(int i=1;i<s.length();i++)
        {
            if(flag==1)
            {
                s[i]='9';
            }
            if(s[i]<s[i-1]&&flag==0)
            {

                flag=1;

                    s[i-1]=s[i-1]-1;
                i--;
            }
        }
        }
        string ans="";
        flag=0;
        for(int i=0;i<s.length();i++)
            {
                if(s[i]=='0'&&flag==0)
                    continue;
                else
                {
                    flag=1;ans=ans+s[i];
                }
            }
        cout<<"Case #"<<z<<": ";
        cout<<ans<<endl;
    }
}
