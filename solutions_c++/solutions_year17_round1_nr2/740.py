#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<int(n);++i)
typedef long long LL;
int a[64][64], b[64][64];
int R[64];
int upper(LL a, LL b){
    return (a+b-1)/b;
}
vector<pair<int,int>> v;
int cc[64][2];
int main(){
    int T;
    scanf("%d",&T);
    REP(cs,T){
        int N, P;
        scanf("%d%d",&N,&P);
        REP(i,N)scanf("%d",R+i);
        v.clear();
        REP(i,N)REP(j,P){
            int x;
            scanf("%d",&x);
            a[i][j]=upper(10LL*x, R[i]*11LL);
            b[i][j]=10LL*x/(R[i]*9LL);
            if(a[i][j]<=b[i][j]){
                v.push_back(make_pair(a[i][j], -(i+1)));
                v.push_back(make_pair(b[i][j], (i+1)));
            }
        }
        /*
        REP(i,N){
            REP(j,P)printf("(%d,%d)", a[i][j], b[i][j]);
            printf("\n");
        }
        */
        sort(v.begin(), v.end());
        memset(cc, 0, sizeof cc);
        int ans=0;
        for(int i = 0; i < v.size();) {
            int p = v[i].first;
            for(; i<v.size() && v[i].first==p && v[i].second<0; ++i) {
                cc[-v[i].second][0]++;
            }
            int mi=11234567;
            for(int j=1;j<=N;++j){
                mi=min(mi, cc[j][0]);
            }
            if(mi>0){
                ans+=mi;
                for(int j=1;j<=N;++j){
                    cc[j][0]-=mi;
                    cc[j][1]+=mi;
                }
            }
            for(; i<v.size() && v[i].first==p && v[i].second>0; ++i) {
                int j=v[i].second;
                if(cc[j][1]>0)cc[j][1]--;
                else cc[j][0]--;
            }
        }
        printf("Case #%d: %d\n", cs+1, ans);
    }
}
