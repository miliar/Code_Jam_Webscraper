#include <bits/stdc++.h>

using namespace std;

long long val(string s)
{
    char a[100];
    for (int i=0;i<=s.size();i++)
        a[i]=s[i];
    long long x;
    x=atoi(a);
    return x;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,i=1;
    cin>>t;
    while (t)
    {
    string s,s1;
    cin>>s;
    s1="";
    long long ans1=0,ans2;
    s1=s;
    for (int i=0;i<s.size()-1;i++)
    {
        if (s[i]>s[i+1])
        {
            if (s[i]=='1')
            {
                s1="";
                for (int j=1;j<s.size();j++)
                    s1=s1+"9";
                    break;
            }
            else
            {
                s1=s;
                int p=0;
                for (int j=i;j>=0;j--)
                if (s1[i]!=s1[j]) {p=j+1; break;}
                s1[p]=s1[p]-1;
                for (int j=p+1;j<s.size();j++)
                    s1[j]='9';
                    break;
            }
        }
        else s1=s;
    }
    ans2=val(s1);
    cout<<"Case #"<<i<<": "<<s1<<endl;
    i++; t--;
    }
    return 0;
}
