#include <bits/stdc++.h>
#define va first.first
#define vb first.second
#define vc second
#define mp make_pair
using namespace std;
typedef pair<int,int> pii;
typedef pair<pii,int> par;
vector<par> V;
vector<int> A[2];
int main(){
    freopen("B-large (1).in","rt",stdin);
    freopen("B-large-output.out","wt",stdout);
    int T;cin>>T;
    for(int f=1;f<=T;f++){
        V.clear();
        int ac[2], tm[2]={720,720}; cin>>ac[0]>>ac[1];
        for(int m=0;m<2;m++){
        A[m].clear();
        for(int i=0;i<ac[m];i++){
            pii u; cin>>u.first>>u.second;
            V.push_back(mp(u,m));
            tm[m]-=(u.second-u.first);
        }
        }
        sort(V.begin(),V.end());
        //for(auto u : V) printf("u=%d %d %d\n",u.va,u.vb,u.vc);
        int exc=0,sz=V.size()-1;
        for(int i=0;i<sz;i++)
            if(V[i].vc==V[i+1].vc) A[V[i].vc].push_back(V[i+1].va-V[i].vb);
        if(V[sz].vc==V[0].vc) A[V[0].vc].push_back((V[0].va-V[sz].vb+1440)%1440);
        int lig=0;
        for(int m=0;m<2;m++){
            //for(auto u : A[m]) printf("A[%d]=%d\n",m,u);
            sort(A[m].begin(),A[m].end());
            for(int u : A[m]){
                if(u>tm[m]) break;
                ++lig;
                tm[m]-=u;
            }
        }

        printf("Case #%d: %d\n",f,V.size()+A[0].size()+A[1].size()-2*lig);
    }
}
