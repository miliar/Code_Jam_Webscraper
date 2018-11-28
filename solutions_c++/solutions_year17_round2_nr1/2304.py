#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    freopen("A_large.txt", "r", stdin);
    freopen("A_large_out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int t=1 ; t<=T ; ++t){
        double D, N, t1, t2;
        cin>>D>>N;
        vector<pair<double, double> > arr(N);
        for(int i=0 ; i<N ; ++i){
            cin>>t1>>t2;
            arr[i] = {t1, t2};
        }
        double ct=0;
        sort(arr.begin(), arr.end());
        for(int i=N-1 ; i>=0 ; --i){
            ct = max(ct, (D-arr[i].first)/arr[i].second);
        }
        cout<<fixed<<setprecision(10)<<"Case #"<<t<<": "<<D/ct<<endl;
    }
}
