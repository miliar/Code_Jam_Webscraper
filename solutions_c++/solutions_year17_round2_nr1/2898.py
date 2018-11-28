#include<bits/stdc++.h>
using namespace std;

int main(){
    long long int i,j,k,x,y,z,n,a,d,t,T;
    double p,q,r,result,tm;
    cin>>T;
    t=1;

    while(t<=T){
        cin>>d>>n; 
        vector<int> a(n), s(n);
        tm=0;
        for(i=0;i<n;i++){
            cin>>q>>r;
            
            p=(((double)d-q)/r);
            tm=max(tm,p);
        }

        result=((double)d/tm);
        
        printf("Case #%lld: %.6f\n",t,result);
        t++;
    }

    return 0;
}
