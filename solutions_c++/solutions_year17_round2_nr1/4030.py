#include<bits/stdc++.h>
#define EPS 1e-10
using namespace std;
typedef long double ld;
int main(){
    ios_base::sync_with_stdio(0);
    int tc,cc,d,n;
    ld x,y,t,a,b,dist,t2;
    cin>>tc;
    for(cc=1;cc<=tc;++cc){
        cin>>d>>n;
        cout<<"Case #"<<cc<<": ";
        if(n==1){
            cin>>x>>y;
            t=(d-x)/y;
            cout<<setprecision(8)<<fixed<<d/t<<'\n';
        }
        else{
            cin>>x>>y>>a>>b;
            if(x-a>EPS){
                swap(x,a);
                swap(y,b);
            }
            if(y-b>0){
                t=(a-x)/(y-b);
                dist=t*y;
                if(dist+x-d>-EPS){
                    t=(d-x)/y;
                    cout<<setprecision(8)<<fixed<<d/t<<'\n';
                }
                else{
                    t2=(d-x-dist)/b;
                    cout<<setprecision(8)<<fixed<<d/(t+t2)<<'\n';
                }
            }
            else{
                t=(d-x)/y;
                cout<<setprecision(8)<<fixed<<d/t<<'\n';
            }
        }
    }
    return 0;
}
