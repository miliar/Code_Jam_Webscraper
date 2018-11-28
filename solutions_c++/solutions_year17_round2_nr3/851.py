#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("be.txt","r",stdin);
    freopen("ki.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=0;tc<t;tc++) {
        int dist[100];
        long double dp[100];
        int lod[100];
        int lov[100];
        int n, q;
        cin>>n>>q;
        for(int i=0; i<n; i++) {
            cin>>lod[i]>>lov[i];
        }
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                int r;
                cin>>r;
                if(j==i+1) {
                    dist[i]=r;
                }
            }
        }
        int z; cin>>z>>z;
        dp[n-1]=0.00000000000;
        for(int i=n-2;i>=0;i--) {
            long double mini=1000000000000000000.0;
            int able=lod[i]-dist[i];
            int it=i+1;
            int far=dist[i];
            while(able>=0 && it<n) {
                long double t_now=(dp[it]+(long double)far/(long double)lov[i]);
                if(t_now<mini) {
                    mini=t_now;
                }
                able-=dist[it];
                far+=dist[it];
                it++;
            }
            dp[i]=mini;
        }
        cout<<"Case #"<<tc+1<<": "<<fixed<<setprecision(10)<<dp[0]<<endl;
    }
    return 0;
}
