#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef pair<int,int> pii;

string solve()
{
    string ans;
    pair<int,char> cnt[3];
    int n,r,o,y,g,b,v,k,cur;
    cin>>n>>r>>o>>y>>g>>b>>v;
    cnt[0] = MP(r,'R');
    cnt[1] = MP(y,'Y');
    cnt[2] = MP(b,'B');
    sort(cnt,cnt+3,greater<pair<int,char>>());

    if (cnt[0].first>n/2)
    {
        return "IMPOSSIBLE";
    }
    ans = "";
    ans += cnt[0].second;
    cnt[0].first--;
    k = cnt[1].first-cnt[2].first;
    for (int i=1;i<=k;i++)
    {
        ans += cnt[1].second;
        cnt[1].first--;
        if (cnt[0].first)
        {
            ans += cnt[0].second;
            cnt[0].first--;
        }
    }
    cur = 2;
    for (int i=0;i<2*cnt[2].first;i++)
    {
        ans += cnt[cur].second;
        if (cur==2) cur = 1; else cur = 2;
        if (cnt[0].first)
        {
            ans += cnt[0].second;
            cnt[0].first--;
        }
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);

    #ifdef _FILES
        freopen("B-small-attempt0.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif // _FILES
    int T;
    cin>>T;
    for (int test=1;test<=T;test++)
    {
        cout<<"Case #"<<test<<": "<<solve()<<endl;
    }
    return 0;
}
