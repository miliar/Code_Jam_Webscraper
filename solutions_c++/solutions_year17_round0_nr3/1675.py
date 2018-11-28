#include <bits/stdc++.h>
using namespace std;

int main() {
    long long int t;
    scanf("%lld",&t);
    int c=0;
    while(t--){
        c++;
         long long int n,k;
         cin>>n>>k;
         long long int nm,xm,nnm=1,nxm=1,ansnm=0,ansxm=0,t_counter=1,p=1;
        if(n%2==1) {
            nm=n/2;
            xm=n/2;

        }
        else {
            xm=n/2;
            nm=xm-1;
        }
        if(k==1){
            cout<<"Case #"<<c<<": "<<xm<<" "<<nm<<endl;
            continue;
        }
        while(xm>0){

             long long int inc=pow(2,p),nt_counter=t_counter+inc;
             if(k>t_counter && k<=nt_counter){
             if(k<=t_counter+nxm) {
                if(xm%2==0) {
                    ansxm=xm/2;
                    ansnm=ansxm-1;

                }
                 else{
                     ansxm=xm/2;
                     ansnm=xm/2;
                 }
             }
                 else{
                    if(nm%2==0) {
                    ansxm=nm/2;
                    ansnm=ansxm-1;

                }
                 else{
                     ansxm=nm/2;
                     ansnm=nm/2;
                 }
                 }
            break;
            }

            if(xm==nm){
                nnm=nnm*2;
                nxm=nxm*2;
            }
            else{
                 if(nm%2==1) {
                nnm=nnm*2 +nxm;

                         }
            else{
                nxm=nxm*2+nnm;

                }
            }
            if(xm==nm){
                if(nm%2==0) {
                    xm=nm/2;
                    nm=xm-1;
                }
                else{
                    nm=xm/2;
                    xm=xm/2;
                }
            }
            else{
            if(nm%2==1) {
                 nm=nm/2;
                 xm=nm+1;

                         }
            else{
                 nm=nm/2-1;
                 xm=nm+1;
            }
        }
          t_counter=nt_counter;
            p++;

        }

        cout<<"Case #"<<c<<": "<<ansxm<<" "<<ansnm<<endl;
       }

}
