#include <cmath>
#include <cstdio>
#include <map>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <stack>
using namespace std;
#define REP(I,N)   FOR(I,0,N)
#define pb push_back
#define LL long long
#define ff first
#define ss second
map<long long,vector<pair<pair<LL,LL>,LL>>>mp;
vector<pair<pair<LL,LL>,LL>> chk(LL n)
{
    if(mp.find(n)!=mp.end())
        return mp[n];
    vector<pair<pair<LL,LL>,LL>> v,d,k;
    if(n==1)
    {
        pair<pair<LL,LL>,LL>p;
        p.ff.ff = 0;
        p.ff.ss = 0;
        p.ss = 1;
        v.push_back(p);
        return v;
    }
    else if(n==2)
    {
         pair<pair<LL,LL>,LL>p;
        p.ff.ff = 1;
        p.ff.ss = 0;
        p.ss = 1;
        v.push_back(p);
        p.ff.ff = 0;
        p.ff.ss = 0;
        p.ss = 1;
        v.push_back(p);
        return v;
    }
    else if(n%2==0)
    {
        pair<pair<LL,LL>,LL>p;
        p.ff.ff = n/2;
        p.ff.ss = n/2 - 1;
        p.ss = 1;
        v.push_back(p);
        d = chk(n/2);
        k =chk(n/2 - 1);

        for(LL i=0; i<d.size(); i++)
        {

            LL t=0;
            for(LL j=0; j<k.size(); j++)
            {
                if(d[i].ff.ff == k[j].ff.ff && d[i].ff.ss == k[j].ff.ss)
                    d[i].ss+=k[j].ss;

            }

            v.push_back(d[i]);
        }
        for(LL i=0; i<k.size(); i++)
        {

            LL t=0;
            for(LL j=0; j<d.size(); j++)
            {
                if(k[i].ff.ff == d[j].ff.ff && k[i].ff.ss == d[j].ff.ss)
                    t++;

            }
            if(!t)
            v.push_back(k[i]);
        }

    }
    else
    {
        pair<pair<LL,LL>,LL>p;
        p.ff.ff = n/2;
        p.ff.ss = n/2;
        p.ss = 1;
        v.push_back(p);
        d = chk(n/2);
        for(LL i=0; i<d.size(); i++)
        {
            pair<pair<LL,LL>,LL>p;
            p=d[i];
            p.ss*=2;
            v.push_back(p);
        }

    }
return mp[n]=v;
}
int main()
{
    freopen("inp.txt","r",stdin);
     freopen("out3.txt","w",stdout);
    int tcase;
    cin>>tcase;
    int f=0;
    for(int tc=1; tc<=tcase; tc++)
    {

        LL n,m;
        cin>>n>>m;
          vector<pair<pair<LL,LL>,LL>> f= chk(n);
          sort(f.begin(),f.end());

        for(int i=f.size()-1; i>=0; i--)
        {
          if(m - f[i].ss<=0)
          {
              cout<<"Case #"<<tc<<": "<<max(f[i].ff.ff,f[i].ff.ss)<<" "<<min(f[i].ff.ff,f[i].ff.ss)<<endl;
              break;
          }
          m-=f[i].ss;
        }
        mp.clear();


    }
    return 0;
}


