#include <bits/stdc++.h>
using namespace std;

string str(long long a)
{
    string s="";
    while (a)
    {
        s+=('0'+a%10);
        a/=10;
    }
    reverse(s.begin(), s.end());
    return s;
}

bool isgood(string s)
{
    int n=s.size();
    for (int i=1; i<n; i++)
        if (s[i]<s[i-1])
            return false;
    return true;
}

long long dec(string s, int len=-1)
{
    if (len==-1)
        len=s.size();
    long long res=0;
    for (int i=0; i<len; i++)
        res=res*10+(s[i]-'0');
    return res;
}

bool isgood(long long a)
{
    return isgood(str(a));
}

void decrement(string &s, int pos)
{
    for (int i=pos-1; i>=0; i--)
        if (s[i]>'0')
        {
            s[i]--;
            break;
        }
        else s[i]='9';
}

int main()
{
    int t;
    cin>>t;
    for (int ii=1; ii<=t; ii++)
    {
        string sn;
        cin>>sn;
        int len=sn.size();
        cout<<"Case #"<<ii<<": ";

        for (int i=len-1; i>=0; i--)
        {
            if (isgood(sn))
            {
                cout<<dec(sn)<<endl;
                break;
            }
            else
            {
                sn[i]='9';
                decrement(sn,i);
            }
        }

    }
}
