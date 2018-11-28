#include <bits/stdc++.h>


using namespace std;

string flip(string s,int start,int k)
{

    for(int i=start;i<s.length()&&i<start+k;i++)
    {
        if(s[i]=='-')
            s[i]='+';
        else
            s[i]='-';

    }
    return s;

}

int main()
{

freopen("A-large.in","r",stdin);
freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int r=0;
    while(t--)
    {
        r++;
    string s;
    cin>>s;
    int k;
    cin>>k;
    int count=0;
    for(int i=0;i<=s.length()-k;i++)
    {
        if(s[i]=='-')
        {
            s=flip(s,i,k);
            count++;
     //       cout<<s<<endl;
        }
    }
    int flag=0;
    for(int i=s.length()-1;i>=0;i--)
    {
        if(s[i]=='-')
        {
            flag=1;
        }
    }
if(flag==0)
cout<<"Case #"<<r<<": "<<count<<endl;
else
cout<<"Case #"<<r<<": "<<"IMPOSSIBLE"<<endl;

    }

}
