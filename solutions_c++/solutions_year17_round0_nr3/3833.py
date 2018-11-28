#include <bits/stdc++.h>

#define mem(a,b) memset(a,b,sizeof(a))
#define rep(i,a,b) for(int i=a;i<b;i++)
const int INF=0x3f3f3f3f;
const int maxn=1e3+5;
const int mod=9901;
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
typedef long long ll;
typedef unsigned int ui;
using namespace std;
ll n,k;
struct Node{
    ll l,r;
    ll len;
    Node() {}

    Node(ll l, ll r) : l(l), r(r) {len=r-l+1;}

    bool operator<(const Node &rhs) const{
        if(len!=rhs.len) return len<rhs.len;
        return l>rhs.l;
    }
};

ll maxs,mins;
void solve(){
    priority_queue<Node> qu;
    qu.push(Node(1,n));
    ll tot=0;
    while(1){
        Node tp=qu.top();
        qu.pop();
        tot++;
        //printf("%lld %lld %lld\n",tot,tp.l,tp.r);
        if(tot==k){
            if(tp.len & 1) maxs=mins=tp.len/2;
            else maxs=tp.len/2,mins=maxs-1;
            return;
        }
        if(tp.len==1) continue;
        ll lPos=tp.l+(tp.len-1)/2;
        qu.push(Node(tp.l,lPos-1));
        qu.push(Node(lPos+1,tp.r));
    }
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("d:\\C-small-2-attempt0.in","r",stdin);
    freopen("d:\\out2.txt","w",stdout);
#endif
    int T; cin>>T;
    for(int cs=1;cs<=T;cs++){
        cin>>n>>k;
        solve();
        printf("Case #%d: ",cs);
        printf("%lld %lld\n",maxs,mins);
        //cout<<bl(n)<<endl;
    }
    return 0;
}