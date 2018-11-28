#include<bits/stdc++.h>
using namespace std;
#define debug
const double pi=3.14159265358979323846264338;
struct node{
    long long r, h;
    node(){}
    node(long long r_, long long h_){
        r=r_;
        h=h_;
    }
    const bool operator < (const node & b) const {
        return r*h>b.h*b.r;
    }
};

vector<node> cakes;
int main(){
#ifdef debug
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif
    int T, cas=0;
    cin>>T;
    while(T--){
        int N, K;
        cin>>N>>K;
        cakes.clear(); cakes.resize(N);
        for(int i=0; i<N; ++i){
            cin>>cakes[i].r>>cakes[i].h;
        }
        double ans=0.;
        for(int i=0; i<N; ++i){
            multiset<node> st;
            double ret=pi*cakes[i].r*cakes[i].r+2.*pi*cakes[i].r*cakes[i].h;
            for(int j=0; j<N; ++j){
                if(j!=i && cakes[j].r<=cakes[i].r)
                    st.insert(cakes[j]);
            }
//            cout<<i<<" "<<cakes[i].r<<" "<<cakes[i].h<<" "<<N<<" "<<K<<endl;
            int cnt=1;
            for(set<node>::iterator it=st.begin(); it!=st.end(); ++it){
                if(cnt==K)
                    break;
//                cout<<it->r<<" "<<it->h<<endl;
                ret+=2.*pi*(it->r)*(it->h);
                ++cnt;
            }
            if(cnt!=K)
                continue;
            ans=max(ans, ret);
 //           cout<<ans<<" "<<ret<<endl;
        }
 //       cout<<ans<<endl;
        cout.precision(9);
        cout<<"Case #"<<++cas<<": "<<fixed<<ans<<endl;
    }
    return 0;
}
