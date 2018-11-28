#include <bits/stdc++.h>
using namespace std;

const int N = 1e2+1;

long double h_dist[N],h_speed[N],dis[N];

long double ans = -1;


void rec(int node, int n, int hr, long double dist, long double cu){
    if(node==n){
        if(ans==-1){
            ans=dist;
        }else{
            ans=min(ans,dist);
        }
    }else{
        if(cu+dis[node] <= h_dist[hr]){
            rec(node+1,n,hr,dist+dis[node]/h_speed[hr],cu+dis[node]);
        }
        if(h_dist[node] >= dis[node]) rec(node+1,n,node,dist+dis[node]/h_speed[node],dis[node]);
    }
}

int main(){
    freopen("input.in","r",stdin);
    freopen("gcb_out3.txt","w",stdout);
    int t;
    int k=0;
    cin>>t;
    while(t--){
            k++;
        int n,q;
        ans = -1;
        cin>>n>>q;
        for(int i=1; i<=n; i++){
            cin>>h_dist[i]>>h_speed[i];
        }
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                int x; cin>>x;
                if(x!=-1){
                    dis[i]=x;
                }
            }
        }
        rec(1,n,1,0,0);
        for(int i=1; i<=q; i++){
            int x,y;cin>>x>>y;
            cout << "Case #" << k << ": " << setprecision(30) << ans << endl;
        }
    }
}
