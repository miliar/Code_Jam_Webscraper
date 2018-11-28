#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("C:\\Downloads\\Documents\\Downloads\\A.in","r",stdin);
    freopen("C:\\Downloads\\Documents\\Downloads\\out.txt","w",stdout);
    int t;
    cin>>t;
    int h=1;
    while(t--)
    {
        string s;
        cin>>s;
        int k;
        cin>>k;
        int ct=0;
        for(int i=0;i<=s.length()-k;i++)
        {
            if(s[i]=='-')
            {
                ct++;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
            }
        }
        int f=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
                f=1;
        }
        cout<<"Case "<<"#"<<h++<<":"<<" ";
        if(f)
            cout<<"IMPOSSIBLE\n";
            else
                cout<<ct<<"\n";
    }
    return 0;
}
