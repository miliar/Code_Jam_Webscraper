#include <iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cstring>
#include<set>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<utility>
#include<map>
#include<functional>
#define rep(i,l,r) for(int i=l;i<r;i++)
#define down(i,l,r) for(int i=l;i>r;i--)
#define pb(x) push_back(x)
#define mp(a,b) make_pair(a,b)
#define ll long long
#define pii pair<int,int>
using namespace std;
string s;
ll int fun(ll int start,ll int last,ll int len)
{
    if(start==last)
    {
        if(s[last]>=s[last-1])
        {
            return -2;
        }
        else
        {
            char z=s[last];
            --z;
            char x=s[last-1];
            if(z>=x)
            {
                return last;
            }
            else
            {
                return -1;
            }
        }
    }
    if(s[start]<s[start-1])
    {
        return -1;
    }
    ll int flag=fun(start+1,last,len-1);
    if(flag==-2)
    {
        return -2;
    }
    if(flag==-1)
    {
            char z=s[start];
            --z;
            char x=s[start-1];
            if(z>=x)
            {
                return start;
            }
            else
            {
                return -1;
            }
    }
    return flag;
}

int main()
{
    ios_base::sync_with_stdio(false);
    fstream ci,co;
    ci.open("B-large.in",ios::in|ios::binary);
    co.open("Bout.txt",ios::out);
    ll int q;
    ci>>q;
    rep(t,1,q+1)
    {

        ci>>s;
        ll int slen=s.length();
        if(slen==1)
        {
            co<<"Case #"<<t<<": "<<s<<endl;
            continue;
        }
        string a1;
        char w=s[0];
        --w;
        a1.pb(w);
        rep(i,1,slen)
        {
            a1.pb('9');
        }
        string a2;
        ll int flag=0;
        ll int f;
        if(s[0]>s[1])
        {
            f=-1;
        }
        else
        {
            f=fun(1,slen-1,slen-1);
        }
        if(f==-2)
        {
            if(s[1]<s[0])
            {
                f=-1;
            }
        }
        if(f==-1 || f==0)
        {
            if(a1[0]=='0')
            {
                a1.erase(0,1);
            }
            co<<"Case #"<<t<<": "<<a1<<endl;
        }
        else
        {
            if(f==-2)
            {
                co<<"Case #"<<t<<": "<<s<<endl;
            }
            else
            {
                string a2;
                rep(i,0,f)
                {
                    a2.pb(s[i]);
                }
                char r=s[f];
                --r;
                a2.pb(r);
                rep(i,f+1,slen)
                {
                    a2.pb('9');
                }
                co<<"Case #"<<t<<": "<<a2<<endl;
            }
        }

    }
}
