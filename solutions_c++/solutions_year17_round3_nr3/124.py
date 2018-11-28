#include<bits/stdc++.h>
using namespace std;

#define int long long

#define rep(i,n) for(int i=0;i<(n);i++)
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define fi first
#define se second
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;

template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

const int LIM=2500;

void solve(){
    int N,K;
    cin>>N>>K;
    double U;
    cin>>U;
    vector<double>P(N);
    rep(i,N)cin>>P[i];

    vector<double> dP(N);
    rep(i,N){
        double tmp=min(U,1.0-P[i]);
        U-=tmp;
        dP[i]=tmp;
    }

    for(int i=0;i<=LIM;i++){
        for(int i=0;i<N;i++){
            for(int j=i+1;j<N;j++){
                double tmp=abs(P[i]-P[j]);
                if(tmp<=dP[i]+dP[j]){
                    tmp=(P[i]+P[j]+dP[i]+dP[j])/2;
                    dP[i]=tmp-P[i];
                    dP[j]=tmp-P[j];
                    continue;
                }
                if(P[i]<P[j]){
                    dP[i]=dP[i]+dP[j];
                    dP[j]=0;
                }
                else{
                    dP[j]=dP[i]+dP[j];
                    dP[i]=0;
                }
            }
        }
    }

    double ans=1.0;
    rep(i,N)ans=ans*(P[i]+dP[i]);
    printf("%.20f\n",ans);

}

signed main(){
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        printf("Case #%lld: ",i);
        solve();
    }
    return 0;
}
