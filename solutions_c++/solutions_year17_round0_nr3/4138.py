#include<bits/stdc++.h>

using namespace std;
#define ll long long





struct Node
{
    ll mi,mx;
    bool operator < (const Node &b) const
    {
        if(mi != b.mi) return mi > b.mi;
        return mx > b.mx;
    }
    bool operator > (const Node &b) const
    {
        if(mi != b.mi) return mi < b.mi;
        return mx < b.mx;
    }
};

ll N,K;
map<Node,ll> mp;



void make(){
    mp.clear();
    priority_queue<Node,vector<Node>,greater<Node> > que;
    if(N&1) que.push((Node){(N-1LL)/2LL,(N-1LL)/2LL});
    else que.push((Node){N/2LL-1LL,N/2LL});
    mp[que.top()] = 1;
    while(!que.empty())
    {
        Node cur = que.top();
        que.pop();
        if(cur.mi)
        {
            if(cur.mi&1)
            {
                Node nxt = (Node){(cur.mi-1LL)/2LL,(cur.mi-1LL)/2LL};
                if(!mp.count(nxt)){
                    que.push(nxt);
                }
                mp[nxt] += mp[cur];
            }else
            {
                Node nxt = (Node){cur.mi/2LL-1LL,cur.mi/2LL};
                if(!mp.count(nxt)){
                    que.push(nxt);
                }
                mp[nxt] += mp[cur];
            }
        }
        if(cur.mx)
        {
            if(cur.mx&1)
            {
                Node nxt = (Node){(cur.mx-1LL)/2LL,(cur.mx-1LL)/2LL};
                if(!mp.count(nxt)){
                    que.push(nxt);
                }
                mp[nxt] += mp[cur];
            }else
            {
                Node nxt = (Node){cur.mx/2LL-1LL,cur.mx/2LL};
                if(!mp.count(nxt))
                    que.push(nxt);
                mp[nxt] += mp[cur];
            }
        }
    }
}

void solve()
{
    make();
    long long acc = 0;
    for(map<Node, long long>::iterator it=mp.begin();it!=mp.end();it++)
    {
        acc += it->second;
        if(acc >= K)
        {
            cout << it->first.mx << ' ' << it->first.mi << '\n';
            return;
        }
    }
}

int main()
{
    //freopen("C.in","r",stdin);
    //freopen("C.out","w",stdout);
    //kkt
    //ittuyityuuty
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        printf("Case #%d: ",cas);
        cin>>N>>K;
        solve();
    }

    return 0;
}
