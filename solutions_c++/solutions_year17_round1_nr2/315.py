#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string.h>
#include <set>
#include <queue>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;


pii kit(int r, int q){
    r*=10;
    q*=10;

    int rmax = r * 11/10;
    int rmin = r * 9/10;

    int resmax = q / rmin;
    int resmin = q / rmax + (q%rmax ? 1 : 0);
    return pii(resmin, resmax);
}

int main(){
    int tcn;
    scanf("%d",&tcn);
    for(int tc=1;tc<=tcn;tc++){
        printf("Case #%d: ",tc);
        int n,p;

        int r[55];
        int q[55][55];
        int ans = 0;
        priority_queue<pii,vector<pii>,greater<pii> > pq[55];
        scanf("%d%d",&n,&p);
        for(int i=0;i<n;i++){
            scanf("%d",&r[i]);
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<p;j++){
                scanf("%d",&q[i][j]);
                pii x = kit(r[i],q[i][j]);
                if(x.first <= x.second)pq[i].push(x);
            }
        }

        while(1){
            int mn = 0, mx = 100000000;
            int ind;
            int flag = 0;
            for(int i=0;i<n;i++){
                if(pq[i].empty()){
                    flag = 1;
                    break;
                }
                pii x = pq[i].top();
                mn = max(mn, x.first);
                if(mx > x.second){
                    mx = x.second;
                    ind = i;
                }
            }
            if(flag)break;
            if(mn <= mx){
                ans++;
                for(int i=0;i<n;i++){
                    pq[i].pop();
                }
            }
            else {
                pq[ind].pop();
            }
        }

        printf("%d\n",ans);
    }
}
