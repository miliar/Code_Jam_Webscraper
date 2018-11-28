#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define CL(A,I) (memset(A,I,sizeof(A)))

#define FOR(i, m, n) for (int i=m; i < n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)

#define D(X) cout<<"  "<<#X": "<<X<<endl;

using ll=long long;
using ii=pair<ll,ll>;
using vi=vector<ll>;
using vii=vector<ii>;

#define aa first
#define bb second

#define EPS (1e-9)
#define EQ(A,B) (A+EPS>B&&A-EPS<B)

int hd,ad,hk,ak,b,d;

struct st{
    int hd,ad,hk,ak;
    int hash(){
        return hd*101*101*101+ad*101*101+hk*101+ak;
    }
};
bitset<114060401> closed;

void process(){
    cin>>hd>>ad>>hk>>ak>>b>>d;

    queue<st> q;
    st s={hd,ad,hk,ak};
    q.push(s);
    q.push({-1});
    closed.reset();
    closed[s.hash()]=0;

    int rnd=1;
    bool ok=0;
    while(q.size()){
        st s = q.front();
        q.pop();

        if(s.hd==-1){
            rnd++;
            if(q.size()==0)break;
            q.push({-1});
            continue;
        }

        // cout<<rnd<<endl;

        if(closed[s.hash()])continue;
        closed[s.hash()]=1;

        if(s.ad>=s.hk){
            ok=1;
            break;
        }

        st ns;

        //attack
        ns={s.hd-s.ak,s.ad,s.hk-s.ad,s.ak};
        if(ns.hd>0 && !closed[ns.hash()])q.push(ns);

        //buff
        ns={s.hd-s.ak,min(s.ad+b,100),s.hk,s.ak};
        if(ns.hd>0 && !closed[ns.hash()])q.push(ns);

        //cure
        ns={hd-s.ak,s.ad,s.hk,s.ak};
        if(ns.hd>0 && !closed[ns.hash()])q.push(ns);

        //debuff
        int dak = max(s.ak-d,0);
        ns={s.hd-dak,s.ad,s.hk,dak};
        if(ns.hd>0 && !closed[ns.hash()])q.push(ns);

    }

    if(ok)cout<<rnd<<endl;
    else cout<<"IMPOSSIBLE"<<endl;

}

int main() {
    int t;cin>>t;
    F(t){
        cout<<"Case #"<<i+1<<": ";
        process();
    }
    return 0;
}