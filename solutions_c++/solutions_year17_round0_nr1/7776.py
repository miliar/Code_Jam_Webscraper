#include <bits/stdc++.h>
using namespace std;
int test;
int k;
string s;
void flip(int ind)
{
    for(int i=ind; i<ind+k; i++)
    {
        if(s[i]=='+') s[i]='-';
        else s[i]='+';
    }
}
bool che()
{
    for(int i=0; i<s.size(); i++)
    {
        if(s[i]=='-') return false;
    }
    return true;
}
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        int ans=0;
        cin>>s>>k;
        for(int i=0; i+k<=s.size(); i++)
        {
            if(s[i]=='-')
            {
                flip(i);
                ans++;
            }
        }
        if(che())
        {
            cout<<"Case #"<<tt<<": "<<ans<<endl;
        }
        else
        {
            cout<<"Case #"<<tt<<": IMPOSSIBLE"<<endl;
        }
    }

    return 0;
}
