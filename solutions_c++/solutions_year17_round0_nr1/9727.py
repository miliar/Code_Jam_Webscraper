#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
void flip(string& s, ll i)
{
    if(s[i]=='+')
    {
        s[i]='-';
    }
    else
    {
        s[i]='+';
    }
}
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    ll t,i,j,ct,it;
    string s;
    ll k;
    cin>>t;
    for(it=1;it<=t;it++)
    {
        cin>>s>>k;
        ct=0;
        for(i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                for(j=0;j<k;j++)
                {
                    flip(s,i+j);
                }
                ct++;
            }
        }
        ll possible=1;
        while(possible==1 && i<s.size())
        {
            if(s[i]=='-')
            {
                possible=0;
            }
            i++;
        }
        cout<<"Case #"<<it<<": ";
        if(possible==1)
        {
            cout<<ct<<endl;
        }
        else
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
}
