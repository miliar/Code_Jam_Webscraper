#include<bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define fileio freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
int main()
{
    fileio
    fastio
    int t,test, k;
    string s;
    cin>>test;
    for(t=1;t<=test;t++)
    {

        cin>>s;
        cin>>k;
        //char f,s;
        int ans=0;
        int len=s.length();
        for(int i=0;i<len-k;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=i;j<(i+k);j++)
                {
                    (s[j]=='-')? (s[j]='+'):(s[j]='-');
                }
            }
        }
        int flag,  f=0;
        if(s[len-k]=='+') flag=0;
        else flag=1;
        for(int i=len-k; i<len;i++)
        {
            if((flag==0) &&(s[i]=='-') ){ cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl; f=1;break;}
            if((flag==1) &&(s[i]=='+') ){ cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl; f=1;break;}
        }
        if(f==0)
        {if(flag==1) ans++;
        cout<<"Case #"<<t<<": "<<ans<<endl;}
    }
    return 0;
}
