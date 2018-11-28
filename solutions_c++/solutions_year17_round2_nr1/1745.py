#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<utility>
#include<iomanip>
using namespace std;

int T,D,N;
long double K[1000];
long double M[1000];
long double ret;
void solve(){
    long double t =0;
    cout<<setprecision(12)<<fixed<<setprecision(12);
    for(int i=0;i<N;i++){
//        cout<<K[i]<<' '<<M[i]<<' '<<D-K[i]<<endl;
        long double tmp=(D-K[i])/M[i];
        if(tmp>t)
            t = tmp;
    }
//    cout <<t<<endl;
    ret = D/t;
}

int main(){
    cin>>T;
    for(int _c=1;_c<=T ; _c++){
        //Input
        cin>>D>>N;
        for(int i=0;i<N;i++)
            cin>>K[i]>>M[i];
        solve();
        cout<<"Case #"<<_c<<": "<<ret<<endl ;
    }
}
