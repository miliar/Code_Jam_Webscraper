#include<bits/stdc++.h>

using namespace std;

int check(string s)
{
    int i=0;
    while(i<(s.size()-1) && s[i]<=s[i+1])i++;
    if(i==s.size()-1)
    return -1;
    else
        return i;
}
string fun(string s,int ind_x)
{
    int i=ind_x;
    s[i]=s[i]-1;
    for(i=i+1;i<s.size();i++)
        s[i]='9';
    return s;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("op3.out","w",stdout);
    int t,ii=1,n;
    cin>>t;
    while(ii<=t)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<ii<<": ";
        for(int x=0;x<s.size();x++)
        {
            int ind_x=check(s);
            if(ind_x==-1);
                //cout<<s;
            else
                s=fun(s,ind_x);
        }
        int x=0;
        string s2;
        while(x<s.size() && s[x]=='0')x++;
        if(x==s.size()-1)
            s2=s;
        else
        {
         for(int i=x;i<s.size();i++)
                s2+=s[i];
        }
        cout<<s2;
        cout<<endl;
        ii++;
    }
}
