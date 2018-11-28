#include<bits/stdc++.h>
using namespace std;
#define redirect_in
#define redirect_out
#define debug

vector<int> pos, speed;

int main(){
#ifdef redirect_in
    freopen("a.in", "r", stdin);
#endif
#ifdef redirect_out
    freopen("a.out", "w", stdout);
#endif
    int T, cas=0;
    cin>>T;
    while(T--){
        int D, N;
        cin>>D>>N;
        pos.clear(); pos.resize(N);
        speed.clear(); speed.resize(N);
        double time=-1;
        for(int i=0; i<N; ++i){
            cin>>pos[i]>>speed[i];
            time=max(time, (D-pos[i])*1./speed[i]);
        }
        cout.precision(6);
        cout<<"Case #"<<++cas<<": "<<fixed<<D/time<<endl;
    }

    return 0;
}
