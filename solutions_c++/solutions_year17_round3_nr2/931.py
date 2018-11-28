#include<bits/stdc++.h>
using namespace std;
#define debug
struct node{
    int l, r;
    node(){}
    node(int l_, int r_):l(l_), r(r_){}
    const bool operator< (const node & b) const {
        return l<b.l;
    }
};
vector<node> C, J;
int main(){
#ifdef debug
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
#endif
    int T, cas=0;
    cin>>T;
    while(T--){
        int NC, NJ;
        cin>>NC>>NJ;
        C.clear(); C.resize(NC);
        J.clear(); J.resize(NJ);
        for(int i=0; i<NC; ++i){
            cin>>C[i].l>>C[i].r;
        }
        sort(C.begin(), C.end());
        for(int i=0; i<NJ; ++i){
            cin>>J[i].l>>J[i].r;
        }
        sort(J.begin(), J.end());
        int ans=0;
        if(NC+NJ==1){
            ans=2;
        }else{
            if(NC==1){
                ans=2;
            }else{
                if(NC==0){
                    C=J;
                }
                if(C[1].r-C[0].l>720&&C[0].r+1440-C[1].l>720){
                    ans=4;
                }else{
                    ans=2;
                }
            }
        }
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
    return 0;
}
