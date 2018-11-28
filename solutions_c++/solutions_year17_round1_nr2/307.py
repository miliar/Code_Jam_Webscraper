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


ll n,p;
ll R[57];
vector<ll> Q[57];

void process(){
    cin>>n>>p;
    F(n)cin>>R[i];
    F(n)Q[i]=vector<ll>(p);
    F(n)FF(p)cin>>Q[i][j];
    F(n)sort(Q[i].begin(), Q[i].end());

    ll maxs=0;
    F(n)FF(p)maxs=max(maxs,(ll)(Q[i][j]*1.1/R[i]));
    maxs+=2;

    int cnt=0;
    while(maxs>0){
        bool ok=1;


        bool end=0;

        F(n)if(Q[i].size()==0)end=1;

        if(end)break;

        // D(Q[0].size())

        // D(maxs)
        // D(Q[0].back()*110)
        // D(100*maxs*R[0])
        F(n)if(!(Q[i].back()*100 >= 90*maxs*R[i]
                && Q[i].back()*100 <= 110*maxs*R[i]))
                ok=0;

        // D(ok)

        if(ok){
            cnt++;
            F(n)Q[i].pop_back();
        }
        else {
            bool ch=0;
            F(n)while(Q[i].size()&&Q[i].back()*100>110*maxs*R[i])Q[i].pop_back(),ch=1;
            F(n)if(Q[i].size()==0)maxs=-1;

            if(ch==0)maxs--;
        }

    }
    cout<<cnt<<endl;

}

int main() {
    int t;cin>>t;
    F(t){
        cout<<"Case #"<<i+1<<": ";
        process();
    }
    return 0;
}