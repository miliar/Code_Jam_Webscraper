/* ***************************************
Author        :Scau.ion
Created Time  :2017/04/15 10:46:10 UTC+8
File Name     :ion.cpp
*************************************** */

#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define ULL unsigned long long
#define PB push_back
#define MP make_pair
#define PII pair<int,int>
#define VI vector<int>
#define VPII vector<PII>
#define X first
#define Y second
#define IOS ios::sync_with_stdio(0);cin.tie(0);
#define IN freopen("C-small-attempt0.in", "r", stdin);
#define OUT freopen("C-small-attempt0.out", "w", stdout);

struct st
{
    int hd,ad,hk,ak;
    bool operator <(const st &b)const
    {
        if (hd!=b.hd) return hd<b.hd;
        if (ad!=b.ad) return ad<b.ad;
        if (hk!=b.hk) return hk<b.hk;
        return ak<b.ak;
    }
};

int check(st x)
{
    if (x.hk<=0) return 1;
    if (x.hd<=0) return -1;
    return 0;
}

int main()
{
    IN;
    OUT;
    IOS;
    int t;
    cin>>t;
    for (int i=1;i<=t;++i)
    {
        st sta;
        int b,d;
        cin>>sta.hd>>sta.ad>>sta.hk>>sta.ak>>b>>d;
        int sh=sta.hd;
        map<st,bool> mp;
        mp[sta]=1;
        queue<pair<st,int> > que;
        que.push(MP(sta,0));
        cout<<"Case #"<<i<<": ";
        bool flag=0;
        while (!que.empty())
        {
            st tis=que.front().X;
            int ro=que.front().Y+1;
            que.pop();

            st nx=tis;
            nx.hk-=nx.ad;
            nx.hd-=nx.ak;
            int res=check(nx);
            if (res==1)
            {
                cout<<ro<<"\n";
                flag=1;
                break;
            }
            else if (res==0)
            {
                if (mp.find(nx)==mp.end())
                {
                    mp[nx]=1;
                    que.push(MP(nx,ro));
                }
            }

            nx=tis;
            nx.ad+=b;
            nx.hd-=nx.ak;
            if (check(nx)==0)
            {
                if (mp.find(nx)==mp.end())
                {
                    mp[nx]=1;
                    que.push(MP(nx,ro));
                }
            }

            nx=tis;
            nx.hd=sh;
            nx.hd-=nx.ak;
            if (check(nx)==0)
            {
                if (mp.find(nx)==mp.end())
                {
                    mp[nx]=1;
                    que.push(MP(nx,ro));
                }
            }

            nx=tis;
            nx.ak=max(0,nx.ak-d);
            nx.hd-=nx.ak;
            if (check(nx)==0)
            {
                if (mp.find(nx)==mp.end())
                {
                    mp[nx]=1;
                    que.push(MP(nx,ro));
                }
            }
        }
        if (!flag) cout<<"IMPOSSIBLE\n";
    }
    cout<<flush;
    return 0;
}
