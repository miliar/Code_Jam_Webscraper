#include<bits/stdc++.h>
using namespace std;
#define debug
vector<double> tmp;
vector<int> v;
int main(){
#ifdef debug
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
#endif
    int T, cas=0;
    cin>>T;
    while(T--){
        int N, K, u;
        double uu, sum=0.;
        cin>>N>>K>>uu;
        u=int(uu*10000+0.5);
        tmp.clear(); tmp.resize(N);
        v.clear(); v.resize(N);
        for(int i=0; i<N; ++i){
            cin>>tmp[i];
            v[i]=int(tmp[i]*10000+0.5);
        }
/*        cout<<u<<" "<<uu<<endl;
        for(int i=0; i<N; ++i){
            cout<<v[i]<<" ";
        }
        cout<<endl;
        for(int i=0; i<N; ++i){
            cout<<tmp[i]<<" ";
        }
        cout<<endl;
*/
        while(u){
            --u;
            int min_pos=-1, min_val=INT_MAX;
            for(int i=0; i<N; ++i){
                if(v[i]<min_val){
                    min_val=v[i];
                    min_pos=i;
                }
            }
            ++v[min_pos];
            tmp[min_pos]+=0.0001;
        }
/*        for(int i=0; i<N; ++i){
            cout<<v[i]<<" ";
        }
        cout<<endl;
        for(int i=0; i<N; ++i){
            cout<<tmp[i]<<" ";
        }
        cout<<endl;
*/
        double ans=1.;
        for(int i=0; i<N; ++i){
            ans*=tmp[i];
        }
        cout.precision(9);
        cout<<"Case #"<<++cas<<": "<<fixed<<ans<<endl;
    }

    return 0;
}
