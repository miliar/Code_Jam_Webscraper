#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("c_small.txt", "r", stdin);
    freopen("c_small_out.txt", "w", stdout);
    int T;
    //T = 100;
    cin>>T;
    for(int t=1 ; t<=T ; ++t){
        int n, k;
        //n = 50, k = 50;
        cin>>n>>k;
        double u;
        vector<double> val(n);
        //u = 50;
        cin>>u;
        int niter = (u+0.00001)*10000;
        //cout<<niter<<endl;
        for(int i=0 ; i<n ; ++i){
            //val[i] = 0.0;
            cin>>val[i];
        }
        for(int i=0 ; i<niter ; ++i){
            sort(val.begin(), val.end());
            val[0] += 0.0001;
        }
        //val[0] -= 0.0001;
        /*for(auto it:val)
            cout<<it<<" ";
        cout<<endl;*/
        double ans = 1;
        for(int i=0 ; i<k ; ++i)
            ans *= val[i];
        cout<<"Case #"<<t<<": "<<fixed<<setprecision(9)<<ans<<endl;

    }
}
