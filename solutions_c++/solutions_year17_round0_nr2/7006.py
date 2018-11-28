#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <sstream>
using namespace std;

typedef long long ll;

const int maxn=1005;

//判断函数
bool judge(ll d)
{
    stringstream ss;
    string s;
    ss<<d;
    ss>>s;
    char maxx='0';
    for(int i=0;i<s.size();i++)
    {
        if(s[i]<maxx)
            return false;
        else
        {
            maxx=s[i];
        }
    }
    return true;
}

ll fun(ll d)
{
    stringstream ss,sd;
    string s;
    ss<<d;
    ss>>s;
    int tmpi=s.size()-1,i=s.size()-1;
    char tmpm=s[tmpi];
    bool flag=0;    //设置标识记录是否需要更改
    i--;
    while(i!=-1)
    {
        if(s[i]>tmpm)
        {
            tmpi=i;
            tmpm=s[i];
            flag=1;
        }
        if(s[i]<tmpm && !flag)
            tmpm=s[i];
        if(flag && s[i]==tmpm)
            tmpi=i;
        i--;
    }
    if(flag)
    {
        s[tmpi]=tmpm-1;
        for(int i=tmpi+1;i<s.size();i++)
            s[i]='9';
    }
    sd<<s;
    ll ret;
    sd>>ret;
    return ret;
}

void solve()
{
    int t;
    cin>>t;
    for(int id=1;id<=t;id++)
    {
        ll d;
        cin>>d;
        printf("Case #%d: %lld\n",id,fun(d));
    }
}


int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    solve();
    return 0;
}
