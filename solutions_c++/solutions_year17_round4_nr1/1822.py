#include <bits/stdc++.h>
#define sz(x) ((int)x.size())
using namespace std;
int main(){
    freopen("A-small-attempt0 (2).in","rt",stdin);
    freopen("Aso.out","wt",stdout);
    int T;cin>>T;
    for(int f=1;f<=T;f++){
        int N,P,ans=0; scanf("%d%d",&N,&P);
        vector<int> m[4];
        for(int i=0;i<N;i++){
            int g; scanf("%d",&g);
            m[g%P].push_back(g);
        }
        ans+=sz(m[0]);
        switch(P){
        case 2:
           ans+= (1+sz(m[1]))/2;
           break;
        case 3:
            ans+= min(sz(m[1]),sz(m[2]));
            ans+= ceil((double)(max(sz(m[1]),sz(m[2]))-min(sz(m[1]),sz(m[2])))/3);
            break;
        }
        printf("Case #%d: %d\n",f,ans);
        fprintf(stderr,"Case #%d: %d\n",f,ans);
    }
}
