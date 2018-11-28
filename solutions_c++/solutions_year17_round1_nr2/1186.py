#include <bits/stdc++.h>
#define F(n) Fi(i,n)
#define Fi(i,n) Fl(i,0,n)
#define Fl(i,l,n) for(int i=l;i<n;i++)
using namespace std;
const int N = 51, P = 51;
int rata[N];
int ingr[N][P];
int idx[N];
typedef pair<int,int> PII;
PII range(int x, int gr){
    float lo = gr*1.1, hi = gr*0.9;
    return PII(ceil(x/lo), floor(x/hi));
}
main(){
    // ios_base::sync_with_stdio(false);
    // cin.tie(0);
    int t,n,p;
    cin>>t;
    Fi(cas, t){
        cin>>n>>p;
        F(n)cin>>rata[i];
        F(n)Fi(j,p)cin>>ingr[i][j];
        F(n)sort(ingr[i],ingr[i]+p);

        int ans = 0;
        memset(idx, 0, sizeof(idx));
        while(idx[0] < p){
            PII r = range(ingr[0][idx[0]], rata[0]);
            if(r.first > r.second)goto FAL;
            for(int j = 1; j < n; j++){
                if(idx[j] >= p)goto FAL;
                while(idx[j] < p){
                    PII r2 = range(ingr[j][idx[j]], rata[j]);
                    if(r2.first > r2.second || r2.second < r.first){
                        idx[j]++;
                        if(idx[j] >= p)goto FAL;
                        continue;
                    }
                    if(r.second < r2.first){
                        goto FAL;
                    }
                    r.first = max(r.first, r2.first);
                    r.second = min(r.second, r2.second);
                    idx[j]++;
                    break;
                }
            }
            ans++;
        FAL:
            idx[0]++;
        }

        cout<<"Case #"<<cas+1<<": "<<ans<<"\n";
        cout<<flush;
    }
}