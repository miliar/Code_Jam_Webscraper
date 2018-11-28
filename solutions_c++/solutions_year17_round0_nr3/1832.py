#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef pair<int,int> pii;

pair<ll,ll> divide(ll len)
{
    if (len==1) return MP(0,0);
    if (len==2) return MP(1,0);
    if (len&1) return MP(len/2,len/2);
    return MP(len/2,len/2-1);
}

pair<ll,ll> solve()
{
    ll n, k;
    pair<ll,ll> cur, pr;
    vector< pair<ll,ll> > seg, buff;
    cin>>n>>k;
    seg.PB(MP(n,1));
    for (;;)
    {
        cur = seg[seg.size()-1];
        if (cur.second>=k) return divide(cur.first);
        k-=cur.second;
        buff.clear();
        for (int i=0;i<seg.size()-1;i++) buff.PB(seg[i]);
        pr = divide(cur.first);
        buff.PB(MP(pr.first,cur.second));
        buff.PB(MP(pr.second,cur.second));
        sort(buff.begin(),buff.end());
        seg.clear();
        seg.PB(buff[buff.size()-1]);
        for (int i=buff.size()-2;i>=0;i--)
        {
            if (!buff[i].first) break;
            if (buff[i].first==buff[i+1].first)
            {
                seg[seg.size()-1].second += buff[i].second;
            }
            else
            {
                seg.PB(MP(buff[i].first,buff[i].second));
            }
        }
        sort(seg.begin(),seg.end());
    }
}

int main()
{
    ios_base::sync_with_stdio(false);

    #ifdef _FILES
        freopen("C-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif // _FILES
    int T;
    pair<ll,ll> res;
    cin>>T;
    for (int test=1;test<=T;test++)
    {
        res = solve();
        cout<<"Case #"<<test<<": "<<res.first<<" "<<res.second<<endl;
    }

    return 0;
}
