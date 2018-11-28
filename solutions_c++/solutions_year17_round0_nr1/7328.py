#include <bits/stdc++.h>

using namespace std;
bool check(string s)
{
    for(int i=0;i<s.size();i++)
    {
        if(s[i]!='+')return 0;
    }
    return 1;
}
char change(char uv)
{
    if(uv=='+')return '-';
        else return '+';
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;cin>>test;
    int mn=1;
    while(test--)
    {
        //cout<<test<<endl;
        cout<<"Case #"<<mn++<<": ";
        string s;int n;
        cin>>s>>n;
        string t=s;reverse(t.begin(),t.end());
        if(check(s))
        {
            cout<<0<<endl;continue;
        }
        int tt=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='+')continue;
            tt++;
            int st=i,en=i+n-1;
            if(en>=s.size())break;
            for(int j=st;j<=en;j++)s[j]=change(s[j]);
        }
        int ttt=0;
        for(int i=0;i<t.size();i++)
        {
            if(t[i]=='+')continue;
            ttt++;
            int st=i,en=i+n-1;
            if(en>=t.size())break;
            for(int j=st;j<=en;j++)t[j]=change(t[j]);
        }
        if(check(s)&&check(t))cout<<min(tt,ttt)<<endl;
        else if(check(s))cout<<tt<<endl;
        else if(check(t))cout<<ttt<<endl;
        else cout<<"IMPOSSIBLE"<<endl;;
    }
    return 0;
}
