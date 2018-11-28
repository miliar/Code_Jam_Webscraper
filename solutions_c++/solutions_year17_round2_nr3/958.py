#include<bits/stdc++.h>
using namespace std;
//#define CHKR
#define ll long long
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define ARRS int(5e5+500)
#define BARRS int(6e4+600)
#define MAX ((long long)(1e17+1))
#define MMAX ((long long)(1e9+10))
#define HS1 ((long long)(1000001329))
#define HS2 ((long long)(1000001531))
#define MOD ((long long)1000000007ll)
#define SQ 31622780
#define PI 3.14159265358979323846264338327950288419716939937510
#define BG 4294967232ll
#define MH 200008
ll f[600];
ll fx[300][300];
double dg[300][300];
pair<ll,ll> h[ARRS];
set<pair<double,pair<ll,pair<ll,ll> > > > q;
vector<pair<ll,ll> > v[ARRS];

#ifndef CHKR
int main(){
#else
int doit(fstream &in,fstream &out){
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
#endif
    #ifdef KHOKHO
        #ifndef CHKR
        freopen("in.in","r",stdin);
        freopen("out.out","w+",stdout);
        #endif //CHKR
    #endif //KHOKHO
    ll n,m,t,p,k,qu,ts;
    cin>>qu;
    for(int te=1; te<=qu; te++){
        cin>>n>>ts;
        for(int i=0; i<n; i++){
            cin>>h[i].sc>>h[i].fr;
        }
        for(int i=0; i<n; i++){
            v[i].clear();
            for(int j=0; j<n; j++){
                cin>>k;
                if(~k){
                    v[i].pb({j,k});
                }
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                    dg[i][j]=MAX;
            }
        }
        double d;
        ll x,hr,lf;
        for(int i=0; i<n; i++){
            q.insert({0.0,{i,{i,h[i].sc}}});
            memset(fx,0,sizeof(fx));
            while(!q.empty()){
                auto t=*q.begin();
                q.erase(q.begin());
                d=t.fr;
                x=t.sc.fr;
                hr=t.sc.sc.fr;
                lf=t.sc.sc.sc;
               // cout<<d<<" "<<x<<" "<<hr<<" "<<lf<<endl;
                if(fx[x][hr])continue;
                fx[x][hr]=1;
                dg[i][x]=min(dg[i][x],d);
                for(int i=0; i<v[x].size(); i++){
                    if(lf>=v[x][i].sc)
                        q.insert({ d+(1.0*v[x][i].sc/h[hr].fr) ,{ v[x][i].fr,  {  hr  ,lf-v[x][i].sc  }   }   });
                    if(h[x].sc>=v[x][i].sc)
                        q.insert({ d+(1.0*v[x][i].sc/h[x].fr) ,{ v[x][i].fr,  {  x  ,h[x].sc-v[x][i].sc  }   }   });
                }
            }


        }
            ll l,r;
       // cin>>ts;
        cout<<"Case #"<<te<<": ";
        while(ts--){
            cin>>l>>r;
            l--;
            r--;
            printf("%.8f ",dg[l][r]);
        }
        cout<<endl;
    }
    return 0;
}
