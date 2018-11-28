#include <bits/stdc++.h>
#define va first
#define vb second
#define mp make_pair
using namespace std;
pair<int,int> H[1005];
int main(){
    freopen("A-large.in","rt",stdin);
    freopen("output-A-large.out","wt",stdout);
    int T; cin>>T;
    for(int f=1;f<=T;f++){
        int N, D; cin>>D>>N;
        for(int i=0;i<N;i++) cin>>H[i].va>>H[i].vb;
        sort(H,H+N);
        long double ans=1e7;
        long double low=0.0, high=1.1e14;
        while(high-low>1e-6){
            ans=(low+high)*0.5;
            bool flag=true;
            for(int i=0;i<N;i++)
                if(H[i].va*ans<(ans-H[i].vb)*D) flag=false;
            if(flag) low=ans;
            else high=ans;
        }
        printf("Case #%d: %.8lf\n",f,ans);
    }
}
