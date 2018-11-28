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

ll n,k;

ii solve(){
    cin>>n>>k;
    map<ll,ll> pq;
    pq[n]=1;

    while(1){
        auto p = *pq.rbegin();
        k-=p.bb;
        if(k<=0)return {(p.aa)/2,(p.aa-1)/2};
        pq[(p.aa-1)/2]+=p.bb;
        pq[(p.aa)/2]+=p.bb;
        pq.erase(p.aa);
    }

}

int main() {
    int t;cin>>t;
    F(t){
        auto p=solve();
        cout<<"Case #"<<i+1<<": "<<p.aa<<' '<<p.bb<<endl;
    }
    return 0;
}