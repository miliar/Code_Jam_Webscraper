#include <bits/stdc++.h>
using namespace std;




int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
     int D,N,T;
     double h,k;
     cin>>T;
     for(int cs=1;cs<=T;cs++){
        cin>>D>>N;
        double tmp=0;
        while(N--){
            cin>>h>>k;
            double fl=(D-h)/k;
            //if()
            //printf("%.5lf ---\n",fl);
            tmp=max(tmp,fl);

        }
        //cout<<tmp<<endl;
        printf("Case #%d: %.6lf\n",cs,D/tmp);
        //cout<<"Case #"<<cs<<": "<<D/tmp<<endl;

     }
}
